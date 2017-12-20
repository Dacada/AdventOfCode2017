#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import base

class Day(base.Base):
    def redistribute(self, registers):
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

    def parse(self, input):
        return [int(n) for n in input.split() if n]

    def run(self, registers):
        seen_states = set()
        cycles = 0

        while True:
            self.redistribute(registers)
            cycles += 1
            state = tuple(registers)
            if state in seen_states:
                break
            seen_states.add(state)

        return cycles

if __name__ == "__main__":
    Day(6).main()
