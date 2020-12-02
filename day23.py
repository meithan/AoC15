# Day 23: Opening the Turing Lock

# ================================================

def exec_program(program, init_values={}):

  regs = {'a': 0, 'b': 0}
  for r in init_values:
    regs[r] = init_values[r]

  ptr = 0
  max_ptr = len(program) - 1

  # Esecute loop
  while True:

    # Read instructions at ptr
    opcode, args = program[ptr]
    # print(opcode, args)

    # Execute instruction
    if opcode == "hlf":
      regs[args[0]] /= 2
      ptr += 1

    elif opcode == "tpl":
      regs[args[0]] *= 3
      ptr += 1

    elif opcode == "inc":
      regs[args[0]] += 1
      ptr += 1

    elif opcode == "jmp":
      ptr += args[0]

    elif opcode == "jie":
      if regs[args[0]] % 2 == 0:
        ptr += args[1]
      else:
        ptr += 1

    elif opcode == "jio":
      if regs[args[0]] == 1:
        ptr += args[1]
      else:
        ptr += 1

    if ptr > max_ptr:
      break

  return regs


# ================================================

# Read and decode program (puzzle input)
program = []
with open("day23.in") as f:
  for line in f:
    tokens = line.strip().split()
    opcode = tokens[0]
    if opcode == "jmp":
      args = (int(tokens[1]),)
    elif opcode in ["jio", "jie"]:
      args = (tokens[1].strip(","), int(tokens[2]))
    else:
      args = (tokens[1],)
    program.append((opcode, args))

# Part 1: run program with initial values of zero
regs = exec_program(program)
print("Part 1:", regs['b'])

# Part 2: run program with a=1
regs = exec_program(program, {'a': 1})
print("Part 2:", regs['b'])
