#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import day5

class Day(day5.Day):
    def run(self, program):
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

if __name__ == '__main__':
    Day(5).main()
