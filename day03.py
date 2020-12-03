# Advent of Code: Day 3
import operator

import sys
infname = sys.argv[1]
f = open(infname,"r")
directions = f.readline()
f.close()

# Part 1
x = 0
y = 0
presents = {(0,0):1}
for d in directions:
  if d == "<": x -= 1
  elif d == ">": x += 1
  elif d == "^": y += 1
  elif d == "v": y -= 1
  loc = (x,y)
  if loc in presents: presents[loc] += 1
  else: presents[loc] = 1
print "Houses that got presents: %i" % (len(presents))
#sorted_houses = sorted(presents.items(), key=operator.itemgetter(1), reverse=True)
#for house, presents in sorted_houses:
#  print house, presents
  
# Part 1
santa_x = 0
santa_y = 0
robo_x = 0
robo_y = 0
presents = {(0,0):2}
santa_turn = True
for d in directions:
  if santa_turn:
    if d == "<": santa_x -= 1
    elif d == ">": santa_x += 1
    elif d == "^": santa_y += 1
    elif d == "v": santa_y -= 1
    loc = (santa_x,santa_y)
  else:
    if d == "<": robo_x -= 1
    elif d == ">": robo_x += 1
    elif d == "^": robo_y += 1
    elif d == "v": robo_y -= 1
    loc = (robo_x,robo_y)    
  santa_turn = not santa_turn   
  if loc in presents: presents[loc] += 1
  else: presents[loc] = 1
print "Houses that got presents (w/ Robo-Santa): %i" % (len(presents))
  
