
rules = []
with open("day19.in") as f:
  for line in f:
    if "=>" in line:
      tokens = line.split("=>")
      rules.append((tokens[0].strip(), tokens[1].strip()))
    elif len(line) > 1:
      med_mol = line.strip()

# Returns all new molecules obtainable from the given molecule
def find_new(rules, molecule):
  new_mols = set()
  for key, sub in rules:
    for i in range(len(molecule)):
      if molecule[i:i+len(key)] == key:
        new_mol = molecule[:i] + sub + molecule[i+len(key):]
        new_mols.add(new_mol)
  return new_mols

# Part 1

molecules = find_new(rules, med_mol)
print("Part 1:", len(molecules))

# Part 2

# We solve part 2 by solving the reverse problem: getting from the big
# medicine molecule down to just 'e', using the rules in reverse.
# We do a depth-first search, always opening the smallest child first.
# Surprisingly, it works!

rules_rev = [(x[1], x[0]) for x in rules]

def find_shortest_rev(rules, start_mol, target_mol):
  to_check = [(0, start_mol)]
  finished = False
  seen = set()
  while len(to_check) > 0:
    cur_steps, cur_mol = to_check.pop()
    children = find_new(rules, cur_mol)
    for child in sorted(list(children), key=lambda x: len(x), reverse=True):
      if child == target_mol:
        print(len(seen), "checked")
        return cur_steps+1
      if child not in seen:
        seen.add(child)
        to_check.append((cur_steps+1, child))
  return None

steps = find_shortest_rev(rules_rev, med_mol, 'e')
print("Part 2:", steps)
