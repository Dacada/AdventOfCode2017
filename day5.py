#!/usr/bin/python
# -*- encoding:utf-8 -*-

import sys

input = open('input5.txt').read()

def run(input):
    program = [int(n) for n in input.split() if n]
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

def main():
    sys.stdout.write("> ")
    new_input = sys.stdin.read()
    
    if new_input:
        print run(new_input)
    else:
        print run(input)

if __name__ == '__main__':
    main()
