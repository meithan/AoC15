# Advent of Code: Day 2

import sys
infname = sys.argv[1]
f = open(infname,"r")

total_paper = 0
total_ribbon = 0
for line in f:
  [L,W,H] = map(lambda x: int(x), line.split("x"))
  areas = [L*W, L*H, W*H]
  total_paper += 2*sum(areas) + min(areas)
  perims = [2*(L+W), 2*(L+H), 2*(W+H)]
  volume = L*W*H
  total_ribbon +=  min(perims) + volume
f.close()
print "Total wrapping paper: %i ft^2" % total_paper
print "Total ribbon length: %i ft" % total_ribbon
