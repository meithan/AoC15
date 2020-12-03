# Advent of Code: Day 7
import sys

# =============================

class Rule:

  def __init__(self, line):
    self.inputs = []
    self.args = []
    tokens = line.strip().split()
    self.output = tokens[-1]
    if len(tokens) == 3:
      self.cmd = "ASSIGN"
      if tokens[0].isdigit():
        self.inputs = []
        self.args = [int(tokens[0])]
      else:
        self.inputs = [tokens[0]]  
        self.args = []
    elif "NOT" in line:
      self.cmd = "NOT"
      self.inputs = [tokens[1]]
      self.args = []
    elif "AND" in line or "OR" in line:
      if "AND" in line: self.cmd = "AND"
      elif "OR" in line: self.cmd = "OR"
      for token in [tokens[0], tokens[2]]:
        if token.isdigit():
          self.args.append(int(token))
        else:
          self.inputs.append(token)
    elif "LSHIFT" in line or "RSHIFT" in line:
      if "LSHIFT" in line: self.cmd = "LSHIFT"
      elif "RSHIFT" in line: self.cmd = "RSHIFT"      
      self.inputs = [tokens[0]]
      self.args = [int(tokens[2])]
    else:
      raise Exception("Couldn't parse rule!\n%s" % line.strip())
  
  def can_satisfy(self, assigned):
    for inwire in self.inputs:
      if inwire not in assigned:
        return False
    return True

  def evaluate(self, assigned):
    if   self.cmd == "ASSIGN":
      if len(self.inputs) == 0:
        return self.args[0]
      else:
        return assigned[self.inputs[0]]
    elif self.cmd == "LSHIFT":
      return (assigned[self.inputs[0]] << self.args[0]) & 0xffff
    elif self.cmd == "RSHIFT":
      return (assigned[self.inputs[0]] >> self.args[0]) & 0xffff
    elif self.cmd == "NOT":
      return ~assigned[self.inputs[0]]
    elif self.cmd in ["AND","OR"]:
      if len(self.inputs) == 1:
        val1 = self.args[0]
        val2 = assigned[self.inputs[0]]
      elif len(self.inputs) == 2:
        val1  = assigned[self.inputs[0]]
        val2 = assigned[self.inputs[1]]
      if self.cmd == "AND":
        return val1 & val2
      elif self.cmd == "OR":
        return val1 | val2
        
  def __str__(self):
    return "%s = %s, %s, %s" % (self.output, self.cmd, str(self.inputs),\
    str(self.args))

# =============================

# Evaluates the circuit, given the rules
def evaluate_circuit(passed_rules):
  rules = passed_rules[:]
  assigned = {}
  while len(rules) > 0:
    flag = False
    for i in range(len(rules)):
      rule = rules[i]
      if rule.can_satisfy(assigned):
        value = rule.evaluate(assigned)
        assigned[rule.output] = value
        rules.pop(i)
        flag = True
        break
    if not flag:
      print assigned
      raise Exception("No rule can be satisfied!")
  return assigned      

# =============================

f = open(sys.argv[1],"r")
rules = []
for line in f:
  rules.append(Rule(line))

# Part 1
values = evaluate_circuit(rules)
a_val = values["a"]
print "Value of wire a: %i" % (a_val if a_val >= 0 else a_val + 2**16)

# Part 2
for rule in rules:
  if rule.output == "b":
    print rule, "\nchanged to"
    rule.cmd = "ASSIGN"
    rule.inputs = []
    rule.args = [a_val]
    print rule
values = evaluate_circuit(rules)
a_val = values["a"]
print "New value of wire a: %i" % (a_val if a_val >= 0 else a_val + 2**16)

