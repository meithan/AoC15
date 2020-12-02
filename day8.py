# Advent of Code: Day 8
import sys

f = open(sys.argv[1],"r")
diffchars1 = 0
for line in f:
  string = line.strip()
  diffchars1 += 2   # double quotes
  i = 1
  while (i < len(string)-1):
    if string[i] == "\\":
      if string[i+1] in ["\\", '"']:
        diffchars1 += 1
        i += 2
      elif string[i+1] == "x":
        diffchars1 += 3
        i += 4
    else:
      i += 1
print "Char difference 1:", diffchars1

f.seek(0)
diffchars2 = 0
for line in f:
  string = line.strip()
  diffchars2 += 4   # double quotes
  i = 1
  while (i < len(string)-1):
    if string[i] in ["\\", '"']:
      diffchars2 += 1
    i += 1
print "Char difference 2:", diffchars2
