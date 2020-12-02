# Advent of Code: Day 16
import sys

#fname = sys.argv[1]
fname = "input16.txt"

hints_str = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""
hints = {}
for line in hints_str.split("\n"):
    data = line.split(":")
    hints[data[0]] = int(data[1])
print hints

# Part 1
f = open(fname)
for line in f:
    data = line.split()
    sue_num = data[1].strip(":")
    found_Sue = True
    for i in range(2,len(data),2):
        item = data[i].strip(":")
        num = int(data[i+1].strip(","))
        if item in hints and num != hints[item]:
            found_Sue = False
            break
    if found_Sue:
        print "\nPart 1: correct Sue is number %s" % sue_num
        print line.strip()
        break

# Part 2
f.seek(0)
f = open(fname)
for line in f:
    data = line.split()
    sue_num = data[1].strip(":")
    found_Sue = True
    for i in range(2,len(data),2):
        item = data[i].strip(":")
        num = int(data[i+1].strip(","))
        if item in hints:
            if item in ["cats", "trees"]:
                if num <= hints[item]:
                    found_Sue = False
                    break
            elif item in ["pomeranians", "goldfish"]:
                if num >= hints[item]:
                    found_Sue = False
                    break        
            else:
                if num != hints[item]:
                    found_Sue = False
                    break
    if found_Sue:
        print "\nPart 2: correct Sue is number %s" % sue_num
        print line.strip()
        break
