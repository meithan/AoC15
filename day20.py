from math import floor, sqrt

# ---------------------------------------

def part1():

  house = 1
  max_seen = None
  while True:
    presents = 0
    for elf in range(1, int(sqrt(house))+1):
      if house % elf == 0:
        presents += 10*elf
        if house // elf != elf:
          presents += 10*(house//elf)
    if max_seen is None or presents > max_seen:
      max_seen = presents
    if presents >= target:
      print(house, max_seen)
      break
    house += 1
    if house % 100000 == 0:
      print("{:,} {:,}".format(house, max_seen))

  print("Part 1:", house)

# ---------------------------------------

def part1_fast():

  max_house = 1000000

  houses = [0]+[10]*(max_house)
  elf = 2
  while elf <= max_house:
    i = elf
    while i <= max_house:
      houses[i] += elf*10
      i += elf
    if elf % 100000 == 0:
      print("{:,}".format(elf))
    elf += 1

  for j in range(1, max_house+1):
    if houses[j] >= target:
      answer = j
      break

  print("Part 1:", answer)

# ---------------------------------------

def part2():

  max_house = 1000000

  houses = [0]*(max_house+1)
  elf = 1
  while elf <= max_house:
    i = elf
    for j in range(50):
      if i > max_house:
        break
      houses[i] += elf*11
      i += elf
    if elf % 100000 == 0:
      print("{:,}".format(elf))
    elf += 1

  for j in range(1, max_house+1):
    if houses[j] >= target:
      answer = j
      break

  print("Part 2:", answer)


# ======================================

target = 33100000

part1_fast()

part2()
