#!/usr/bin/python
# -*- encoding:utf-8 -*-

import sys
import day8

input = open("input18.txt").read()

class Program(object):
    def __init__(self, instructions):
        self._registers = day8.RegisterBank()
        self.instructions = instructions
        self.program_counter = 0

    def run(self):
        pass

    def _snd(self, x):
        pass

    def _set(self, x, y):
        pass

    

def to_lists(input):
    return [instr.split() for instr in input.split('\n')]

def run(input):
    program = Program(to_lists(input))
    return program.run()

def main():
    sys.stdout.write("> ")
    new_input = sys.stdin.read()

    if new_input:
        print run(new_input)
    else:
        print run(input)

if __name__ == "__main__":
    main()
