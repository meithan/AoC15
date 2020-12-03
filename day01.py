# Advent of Code: Day 1
import sys

infname = sys.argv[1]
f = open(infname,"r")
parens = f.readline()
f.close()

# Parts 1 and 2
floor = 0
base_pos = None
for i,p in enumerate(parens):
  if p == "(": floor += 1
  else: floor -= 1
  if base_pos == None and floor == -1:
    base_pos = i+1
print "Final floor: %i" % floor
print "First basement position: %i" % base_pos

