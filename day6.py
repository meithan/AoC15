# Advent of Code: Day 6
import sys

lights1 = []
lights2 = []
for i in range(1000):
  lights1.append([False]*1000)
  lights2.append([0]*1000)

infname = sys.argv[1]
f = open(infname,"r")
for line in f:
  data = line.strip().split()
  if data[0] == "toggle":
    mode = "toggle"
    x1, y1 = map(int, data[1].split(","))
    x2, y2 = map(int, data[3].split(","))    
  else:
    mode = data[1]
    x1, y1 = map(int, data[2].split(","))
    x2, y2 = map(int, data[4].split(","))
  if x2 < x1:
    tmp = x1
    x1 = x2
    x2 = tmp
  if y2 < y1:
    tmp = y1
    y1 = y2
    y2 = tmp
  for i in range(x1,x2+1):
    for j in range(y1,y2+1):
      if mode == "toggle":
        lights1[i][j] = not lights1[i][j]
        lights2[i][j] += 2
      elif mode == "on":
        lights1[i][j] = True
        lights2[i][j] += 1
      elif mode == "off":
        lights1[i][j] = False
        if lights2[i][j] >= 1: 
          lights2[i][j] -= 1

lights_on1 = 0
brightness2 = 0
for i in range(1000):
  for j in range(1000):
    if lights1[i][j]: lights_on1 += 1
    brightness2 += lights2[i][j]
print "Lights on, part 1: %i" % lights_on1
print "Brightness, part 2: %i" % brightness2




