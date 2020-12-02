# Advent of Code: Day 4
import hashlib

import sys
key = sys.argv[1]

n = 1
found5 = False
found6 = False
while True:
  h = hashlib.md5(key + str(n)).hexdigest()
  if not found5 and h[:5] == "00000":
    print "Found 5-zero hash at %i" % n
    print "md5(%s) = %s" % (key + str(n), h)
    found5 = True
    if found6: break
  if not found6 and h[:6] == "000000":
    print "Found 6-zero hash at %i" % n
    print "md5(%s) = %s" % (key + str(n), h)
    found6 = True
    if found5: break
  n += 1