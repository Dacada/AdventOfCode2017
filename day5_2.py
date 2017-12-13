#!/usr/bin/python
# -*- encoding:utf-8 -*-

import day5

def run(input):
    program = [int(n) for n in input.split() if n]
    pc = 0
    cycles = 0

    try:
        while True:
            old_pc = pc
            pc += program[pc]
            if program[old_pc] >= 3:
                program[old_pc] -= 1
            else:
                program[old_pc] += 1
            cycles += 1
    except IndexError:
        return cycles

day5.run = run

if __name__ == '__main__':
    day5.main()
