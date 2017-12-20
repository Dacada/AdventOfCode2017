#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import base

class Day(base.Base):
    def parse(self, input):
        return [int(n) for n in input.split() if n]
    def run(self, program):
        pc = 0
        cycles = 0;

        try:
            while True:
                old_pc = pc
                pc += program[pc]
                program[old_pc] += 1
                cycles += 1
        except IndexError:
            return cycles

if __name__ == '__main__':
    Day(5).main()
