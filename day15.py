#!/usr/bin/python
# -*- encoding:utf-8 -*-

input = "722 354"

def generator(start, factor):
    prev = start
    while True:
        prev = (prev * factor) % 2147483647
        yield prev

def generatorA(start):
    return generator(start, 16807)
def generatorB(start):
    return generator(start, 48271)

def run(input):
    inputA,inputB = (int(n) for n in input.split())
    
    genA = generatorA(inputA)
    genB = generatorB(inputB)
    count = 0

    for __ in range(40000000):
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
