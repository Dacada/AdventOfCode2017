#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import day6

class Day(day6.Day):
    def run(self, registers):
        seen_states = []

        while True:
            self.redistribute(registers)
            state = tuple(registers)
            if state in seen_states:
                return len(seen_states[seen_states.index(state):])
            seen_states.append(state)

if __name__ == '__main__':
    Day(6).main()
