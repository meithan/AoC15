# Day 24: It Hangs in the Balance

import itertools

weights = []
with open("day24.in") as f:
  for line in f:
    weights.append(int(line))

# Part 1

# The target weight for each group
assert sum(weights) % 3 == 0
target = sum(weights) // 3
print("target=",target)

first_groups = []
combos = itertools.combinations(weights, 6)
for combo in combos:
  if sum(combo) == target:
    QE = 1
    for x in combo:
      QE *= x
    # print(sum(combo), combo, QE)
    first_groups.append((sum(combo), combo, QE))
first_groups.sort(key=lambda x: x[2])

print(first_groups[0])
print("Part 1:", first_groups[0][2])

# Part 2
assert sum(weights) % 4 == 0
target2 = sum(weights) // 4
print("target2=",target2)

first_groups2 = []
combos = itertools.combinations(weights, 5)
for combo in combos:
  if sum(combo) == target2:
    QE = 1
    for x in combo:
      QE *= x
    # print(sum(combo), combo, QE)
    first_groups2.append((sum(combo), combo, QE))
first_groups2.sort(key=lambda x: x[2])

print(first_groups2[0])
print("Part 2:", first_groups2[0][2])
