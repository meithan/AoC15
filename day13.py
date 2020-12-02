import itertools
import sys

#infile = open(sys.argv[1])
infile = open("input13.txt")
lines = []
for line in infile.readlines():
    lines.append(line.strip())
infile.close()

# Parse number of persons and names
npers = 0
names = {}
for line in lines:
    line = line.split()
    person = line[0]
    if person not in names:
        names[person] = npers
        npers += 1
print names

# For Part 2: add myself to the list
part2 = True
if part2:
    for person in names.keys():
        lines.append("%s would gain 0 happiness units by sitting next to Me." % person)
    for person in names.keys():
        lines.append("Me would gain 0 happiness units by sitting next to %s." % person)
    names["Me"] = npers
    npers += 1

# Fill in weights matrix
weights = []
for i in range(npers):
    weights.append([0]*npers)
for line in lines:
    line = line.strip(".").split()
    print line[0], line[2], int(line[3]), line[10]
    weights[names[line[0]]][names[line[10]]] = int(line[3])
    if line[2] != "gain": weights[names[line[0]]][names[line[10]]] *= -1

# Search through all possible seating arrangements
best_arrange = None
best_value = None

print "Evaluating all seating arrangements ..."
count = 0
for perm in itertools.permutations(range(npers)):
    value = 0
    for i in range(npers):
        im = i-1 if i > 0 else npers-1
        ip = i+1 if i <= npers-2 else 0
        value += weights[perm[i]][perm[im]]
        value += weights[perm[i]][perm[ip]]
    if best_value == None or value > best_value:
        best_value = value
        best_arrange = perm
    count += 1
print "%i arrangements evaluated" % count
print "Best happinness: %i" % best_value
print "Best arrangement: %s" % repr(best_arrange)
