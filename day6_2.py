#!/usr/bin/python
# -*- encoding:utf-8 -*-

import day6

def run(input):
    registers = [int(n) for n in input.split() if n]
    seen_states = []

    while True:
        day6.redistribute(registers)
        state = tuple(registers)
        if state in seen_states:
            return len(seen_states[seen_states.index(state):])
        seen_states.append(state)

day6.run = run

if __name__ == '__main__':
    day6.main()
