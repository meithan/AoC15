# Advent of Code: Day 11
import sys

factors = [26**(7-i) for i in range(8)]

def increment(oldpass):
  if oldpass == "zzzzzzzz": return "aaaaaaaa"
  else: return decode(encode(oldpass)+1)

def encode(password):
  value = 0
  for i in range(8):
    value += factors[i] * (ord(password[i]) - 97)
  return value

def decode(value):
  password = ""
  for p in factors:
    d = value // p
    password += chr(97+d)
    value -= p*d
  return password

def isValid(pwrd):
  found_triplet = False
  first_pair = None
  found_pairs = False
  for i in range(8):
    if pwrd[i] in ["i","o","l"]:
      return False
    if not found_triplet and i <= 5:
      if ord(pwrd[i])+1 == ord(pwrd[i+1]) and ord(pwrd[i+1])+1 == ord(pwrd[i+2]):
        found_triplet = True
    if not found_pairs and i <= 6:
      if pwrd[i] == pwrd[i+1]:
        if first_pair == None:
          first_pair = pwrd[i:i+2]
        else:
          if pwrd[i:i+2] != first_pair:
            found_pairs = True
  if found_triplet and found_pairs:
    return True
  else:
    return False
           

password = sys.argv[1]
value = encode(password)
newpass = increment(password)
while not isValid(newpass):
  value += 1
  newpass = decode(value)
print newpass
