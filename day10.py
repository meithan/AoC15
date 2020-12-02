# Advent of Code: Day 10
import sys

# Applies the look and say iteration once
def look_and_say(seq):
  newseq = ""
  i = 1
  cur = seq[0]
  count = 1
  while i <= len(seq)-1:
    if seq[i] == cur:
      count += 1
    elif seq[i] != cur:
      newseq += "%i%s" % (count, cur)
      cur = seq[i]
      count = 1
    i += 1
  newseq += "%i%s" % (count, cur)
  return newseq

sequence = sys.argv[1]
for i in range(50):
  sequence = look_and_say(sequence)
  if i == 39: print "Length ater 40 iterations:", len(sequence)
print "Length ater 50 iterations:", len(sequence)
