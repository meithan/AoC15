# Day 21: RPG Simulator 20XX

# My input
boss_HP = 100
boss_dmg = 8
boss_armor = 2

# Resolves the combat given the player's dmg and armor scores
def combat(player_damage, player_armor):

  player_HP = 100

  player_net_dmg = max(1, player_damage - boss_armor)
  boss_net_dmg = max(1, boss_dmg - player_armor)

  boss_dead_rounds = boss_HP // player_net_dmg
  player_dead_rounds = player_HP // boss_net_dmg

  if boss_dead_rounds <= player_dead_rounds:
    player_HP_left = player_HP - (boss_dead_rounds-1)*boss_net_dmg
    winner = "Player"
    # print("Player wins on round {}; {} HP left".format(boss_dead_rounds, player_HP_left))
  else:
    boss_HP_left = boss_HP - player_dead_rounds*player_net_dmg
    winner = "Boss"
    # print("Boss wins on round {}; {} HP left".format(player_dead_rounds, boss_HP_left))

  return winner

# -----------------------------------------

weapons = [
("Dagger",     8,  4, 0),
("Shortsword", 10, 5, 0),
("Warhammer",  25, 6, 0),
("Longsword",  40, 7, 0),
("Greataxe",   74, 8, 0)
]
armors = [
("No armor",     0, 0, 0),
("Leather",     13, 0, 1),
("Chainmail",   31, 0, 2),
("Splintmail",  53, 0, 3),
("Bandedmail",  75, 0, 4),
("Platemail",  102, 0, 5)
]
rings = [
("No ring",      0, 0, 0),
("Damage +1",   25, 1, 0),
("Damage +2",   50, 2, 0),
("Damage +3",  100, 3, 0),
("Defense +1",  20, 0, 1),
("Defense +2",  40, 0, 2),
("Defense +3",  80, 0, 3)
]

# Generate all possible gear sets
gear_sets = []
for weap in weapons:
  for armor in armors:
    for i in range(7):
      ring1 = rings[i]
      for j in range(i, 7):
        ring2 = rings[j]
        if ring2 == ring1 and ring1 != "No ring":
          continue
        gear_set = [weap, armor, ring1, ring2]
        cost = sum([x[1] for x in gear_set])
        tot_damage = sum([x[2] for x in gear_set])
        tot_armor = sum([x[3] for x in gear_set])
        gear_sets.append((cost, tot_damage, tot_armor, gear_set))

# Sort gear sets by increasing cost
gear_sets.sort(key=lambda gs: gs[0])
print(len(gear_sets))

# --------------------------------------------

def part1():
  for gs in gear_sets:
    cost, player_damage, player_armor = gs[0], gs[1], gs[2]
    winner = combat(player_damage, player_armor)
    # print(cost, player_damage, player_armor, winner)
    if winner == "Player":
      return cost

# --------------------------------------------

def part2():
  max_cost = 0
  for gs in gear_sets:
    cost, player_damage, player_armor = gs[0], gs[1], gs[2]
    winner = combat(player_damage, player_armor)
    # print(cost, player_damage, player_armor, winner)
    if winner == "Boss":
      if cost > max_cost:
        max_cost = cost
  return max_cost

# --------------------------------------------

print("Part 1:", part1())

print("Part 2:", part2())
