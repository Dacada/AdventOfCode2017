#!/usr/bin/python
# -*- encoding:utf-8 -*-

input = "4 1 15 12 0 9 9 5 5 8 7 3 14 5 12 3"

def redistribute(registers):
    max_n = max(registers)
    max_i = registers.index(max_n)
    registers[max_i] = 0

    i = max_i + 1
    while max_n:
        if i >= len(registers):
            i = 0
        registers[i] += 1
        i += 1
        max_n -= 1

def run(input):
    registers = [int(n) for n in input.split() if n]
    seen_states = set()
    cycles = 0

    while True:
        redistribute(registers)
        cycles += 1
        state = tuple(registers)
        if state in seen_states:
            break
        seen_states.add(state)

    return cycles

def main():
    new_input = raw_input("> ")
    if new_input:
        print run(new_input)
    else:
        print run(input)

if __name__ == "__main__":
    main()
