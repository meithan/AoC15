# Advent of Code: Day 5
import sys

def isnice1(string):
  vowels = 0
  has_double = False
  for i in range(len(string)):
    if i < len(string)-1:
      if string[i:i+2] in ["ab", "cd", "pq", "xy"]:
        return False
      if string[i] == string[i+1]:
        has_double = True
    if string[i] in ["a","e","i","o","u"]:
      vowels += 1
  if vowels >= 3 and has_double: return True
  else: return False

def isnice2(string):
  has_double_pair = False
  has_sandwich = False
  for i in range(len(string)-1):
    if not has_double_pair:
      pair = string[i:i+2]
      if (i >= 2 and pair in string[:i]) \
      or (i < len(string)-3 and pair in string[i+2:]):
        has_double_pair = True      
    if not has_sandwich and i < len(string)-2 and string[i] == string[i+2]:
      has_sandwich = True
  if has_double_pair and has_sandwich: return True
  else: return False

nicecount1 = 0
nicecount2 = 0
infname = sys.argv[1]
f = open(infname,"r")
for line in f:
  string = line.strip()
  if isnice1(string): nicecount1 += 1
  if isnice2(string): nicecount2 += 1
f.close()
print "Nice strings 1: %i" % nicecount1
print "Nice strings 2: %i" % nicecount2
      
