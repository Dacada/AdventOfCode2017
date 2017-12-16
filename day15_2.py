#!/usr/bin/python
# -*- encoding:utf-8 -*-

input = "722 354"

def generator(start, factor, filter):
    prev = start
    while True:
        prev = (prev * factor) % 2147483647
        if prev % filter == 0:
            yield prev

def run(input):
    inputA,inputB = (int(n) for n in input.split())
    
    genA = generator(inputA, 16807, 4)
    genB = generator(inputB, 48271, 8)
    count = 0

    for __ in range(5000000):
        a = next(genA) & 0xFFFF
        b = next(genB) & 0xFFFF
        if a == b:
            count += 1

    return count

def main():
    new_input = raw_input("> ")
    if new_input:
        print run(new_input)
    else:
        print run(input)

if __name__ == '__main__':
    main()
