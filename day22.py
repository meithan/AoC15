# Day 22: Wizard Simulator 20XX

# -----------------------------------------

class Player:

  def __init__(self, start_HP, start_armor, start_mana):
    self.start_HP = start_HP
    self.start_armor = start_armor
    self.start_mana = start_mana
    self.reset()

  def reset(self):
    self.HP = self.start_HP
    self.armor = self.start_armor
    self.mana = self.start_mana
    self.mana_spent = 0
    self.active_spells = []
    self.history = []

  def get_avail_spells(self):

    avail_spells = []
    active_names = [x.name for x in self.active_spells]
    for spell_name in spell_names:

      spell = spellbook(spell_name)

      if spell.name in active_names:
        # print("Can't cast {}; it's already active".format(spell.name))
        pass

      elif self.mana < spell.mana_cost:
        # print("Not enough mana to cast {} (req: {}, avail: {})".format(spell.name, spell.mana_cost, player.mana))
        pass

      else:
        avail_spells.append(spell.name)

    return avail_spells

  def cast(self, spell, verbose=False):

    msg = spell.start()
    if verbose:
      s = "Player casts {}".format(spell.name)
      if msg != "":
        s += ", " + msg
      print(s)

    if spell.duration != "instant":
      self.active_spells.append(spell)

    self.mana -= spell.mana_cost
    self.mana_spent += spell.mana_cost

  def apply_effects(self, verbose=False):

    for spell in self.active_spells:

      msg = spell.refresh()

      if verbose and msg != "":
        s = spell.name + " activates, " + msg
        print(s)

      spell.duration -= 1

      if spell.duration > 0:
        if verbose:
          s = "{} has {} turns left".format(spell.name, spell.duration)
      elif spell.duration == 0:
        msg = spell.end()
        if verbose:
          s = "{} wears off".format(spell.name)
          if msg != "":
            s += ", " + msg
          print(s)

    # Keep only still active spells
    self.active_spells = [x for x in self.active_spells if x.duration > 0]

class Boss:
  def __init__(self, start_HP, damage):
    self.start_HP = start_HP
    self.damage = damage
    self.reset()
  def reset(self):
    self.HP = self.start_HP
  def attack(self, verbose=False):
    net_damage = max(1, self.damage - player.armor)
    player.HP -= net_damage
    if verbose:
      print("Boss attacks for {} - {} = {} damage".format(self.damage, player.armor, net_damage))

class Spell:
  def __init__(self):
    pass
  def start(self):
    return ""
  def refresh(self):
    return ""
  def end(self):
    return ""

class MagicMissile(Spell):
  def __init__(self):
    self.name = "Magic Missile"
    self.mana_cost = 53
    self.duration = "instant"
    self.damage = 4
  def start(self):
    msg = "dealing {} damage.".format(self.damage)
    boss.HP -= self.damage
    return msg

class Drain(Spell):
  def __init__(self):
    self.name = "Drain"
    self.mana_cost = 73
    self.duration = "instant"
    self.damage = 2
    self.heal = 2
  def start(self):
    msg = "dealing {} damage and healing {} hit points.".format(self.damage, self.heal)
    player.HP += self.heal
    boss.HP -= self.damage
    return msg

class Shield(Spell):
  def __init__(self):
    self.name = "Shield"
    self.mana_cost = 113
    self.duration = 6
    self.armor = 7
  def start(self):
    msg = "increasing armor by {} for {} turns".format(self.armor, self.duration)
    player.armor += self.armor
    return msg
  def end(self):
    msg = "decreasing armor by {}".format(self.armor)
    player.armor -= self.armor
    return msg

class Poison(Spell):
  def __init__(self):
    self.name = "Poison"
    self.mana_cost = 173
    self.duration = 6
    self.damage = 3
  def start(self):
    return "active for {} turns".format(self.duration)
  def refresh(self):
    msg = "dealing {} damage".format(self.damage)
    boss.HP -= self.damage
    return msg

class Recharge(Spell):
  def __init__(self):
    self.name = "Recharge"
    self.mana_cost = 229
    self.duration = 5
    self.mana = 101
  def start(self):
    return "active for {} turns".format(self.duration)
  def refresh(self):
    msg = "restoring {} mana".format(self.mana)
    player.mana += self.mana
    return msg

spell_names = ["Magic Missile", "Shield", "Recharge", "Poison", "Drain"]

def spellbook(spell_name):

  spell = None
  if spell_name.lower() in ["magic missile", "magic", "missile", "mm", "m"]:
    spell = MagicMissile()
  elif spell_name.lower() in ["drain", "d"]:
    spell = Drain()
  elif spell_name.lower() in ["shield", "s"]:
    spell = Shield()
  elif spell_name.lower() in ["poison", "p"]:
    spell = Poison()
  elif spell_name.lower() in ["recharge", "r"]:
    spell = Recharge()

  if spell is None:
    return None
  else:
    return spell

def do_combat(spells_list, hard_mode=False, pause=False, verbose=False):

  turn = 0
  player.reset()
  boss.reset()
  active = "Player"

  spells_used = []
  next_idx = 0

  while True:

    turn += 1
    if verbose:
      print("\n== Turn {}: {} ==".format(turn, active))
      print("- Player has {} HP, {} armor, {} mana (spent: {})".format(player.HP, player.armor, player.mana, player.mana_spent))
      print("- Boss has {} HP".format(boss.HP))

    player.apply_effects(verbose=verbose)

    if player.HP <= 0:
      if verbose: print("\nThe Player is killed!")
      return "Boss"
    elif boss.HP <= 0:
      if verbose: print("\nThe boss is defeated!")
      return "Player"

    if active == "Player":

      if hard_mode:
        player.HP -= 1
        if player.HP == 0:
          if verbose: print("\nThe Player is killed!")
          return "Boss"

      if player.mana < 52:
        if verbose: print("\nInsufficient mana to cast any more spells! The Player is killed!")
        return "Boss"

      avail_spells = player.get_avail_spells()
      if verbose: print("Available spells:", avail_spells)

      if spells_list == "interactive":
        spell = None
        while spell is None:
          spell_name = input("> Spell to cast: ")
          spell = spellbook(spell_name)
      elif spells_list == "auto":
        pass
      else:
        if next_idx > len(spells_list)-1:
          if verbose: print("\nNo more spells in list! The Player is killed!")
          return "Boss"
        spell = spellbook(spells_list[next_idx])
        if spell.name not in player.get_avail_spells():
          if verbose: print("Can't cast {}".format(spell.name))
          return "Boss"
        next_idx += 1

      player.cast(spell, verbose=verbose)
      player.history.append(spell.name)

      if spells_list != "interactive" and pause:
        input("ENTER to continue")

      active = "Boss"

    elif active == "Boss":

      boss.attack(verbose=verbose)
      active = "Player"

    if player.HP <= 0:
      if verbose: print("\nThe Player is killed!")
      return "Boss"
    elif boss.HP <= 0:
      if verbose: print("\nThe Boss is defeated!")
      return "Player"

def brute_force(hard_mode=False):

  spells = ["Recharge", "Shield", "Poison", "Drain", "Magic Missile"]
  num_spells = 8

  import itertools
  lists = itertools.product(spells, repeat=num_spells)

  count = 0
  best_mana = 1e30
  best_sequences = []
  for spells_list in lists:
    count += 1
    winner = do_combat(spells_list=spells_list, hard_mode=hard_mode)
    if winner == "Player":
      if player.mana_spent == best_mana:
        best_sequences.append(spells_list)
      elif player.mana_spent < best_mana:
        best_mana = player.mana_spent
        best_sequences = [spells_list]
    if count % 100000 == 0:
      print("{:,} {}".format(count, best_mana if best_mana < 1e30 else "None"))

  print("{:,} sequences tried".format(count))
  if best_mana > 1e29:
    print("No winning sequence found")
  else:
    print("Best mana: {}".format(best_mana))
    print("{} sequences found:".format(len(best_sequences)))
    for seq in best_sequences:
      print(seq)


# ===================================================

# My input
boss_start_HP = 51
boss_damage = 9

player_start_HP = 50
player_start_armor = 0
player_start_mana = 500

verbose = False

player = Player(player_start_HP, player_start_armor, player_start_mana)
boss = Boss(boss_start_HP, boss_damage)

brute_force(hard_mode=True)

# spells_list = ('Recharge', 'Poison', 'Shield', 'Magic Missile', 'Poison', 'Magic Missile', 'Magic Missile', 'Magic Missile')
# winner = do_combat(spells_list=spells_list, pause=False, verbose=True)
# print("Mana spent:", player.mana_spent)
