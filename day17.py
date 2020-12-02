# Advent of Code: Day 17
import sys

#fname = sys.argv[1]
fname = "input17.txt"
liters = 150
#fname = "test17.txt"
#liters = 25

f = open(fname)
containers = []
for line in f:
    containers.append(int(line.strip()))
f.close()
print containers
num_conts = len(containers)

count = 0
min_number = None
min_ways = None
for i in range(2**len(containers)):
    mask = ('{0:0%ib}'%num_conts).format(i)
    total = 0
    ncts = 0
    for j in range(num_conts):
        if mask[j] == "1":
            ncts += 1
            total += containers[j]
            if total > liters:
                break
    if total == liters:
        if min_number == None:
            min_number = ncts
            min_ways = 1
        elif ncts == min_number:
            min_ways += 1
        elif ncts < min_number:
            min_number = ncts
            min_ways = 1
        #print mask, [containers[i] for i in range(num_conts) if mask[i] == "1"]
        count += 1
print "Part 1: There are %i ways to distribute the eggnog" % count
print "Part 2: the minimum number of containers is %i, and there are %i ways" % (min_number, min_ways)
