# Day 25: Let It Snow

import re

# =============================================

# Computes the code at sequential position n (counting from 1)
x0 = 20151125
a = 252533
m = 33554393
def compute_code(n):
  # x_n = (x_{n-1} * a) mod m
  x = x0
  for i in range(n-1):
    x = (x * a) % m
  return x

# Converts coordinates (x,y) to a sequential position
def coords_to_seq(x, y):
  return 1 + x*(x-1)//2 + x*(y-1) + y*(y-1)//2

# =============================================

with open("day25.in") as f:
  text = f.readline()
  row = int(re.search("row ([0-9]+)", text).group(1))
  col = int(re.search("column ([0-9]+)", text).group(1))

print(row, col)
pos = coords_to_seq(row, col)
print(pos)

print("Part 1:", compute_code(pos))
