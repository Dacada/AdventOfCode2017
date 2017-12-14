#!/usr/bin/python
# -*- encoding:utf-8 -*-

input = '18,1,0,161,255,137,254,252,14,95,165,33,181,168,2,188'
list = range(256)

def reverse(list, start, length):
    """
    Reverse a slice of the given list in place. The slice is defined by the starting index and the total length. Wrap back to the start if end of list is reached.
    """
    i = start
    j = start + length - 1
    while i < j:
        modi = i % len(list)
        modj = j % len(list)
        tmp = list[modi]
        list[modi] = list[modj]
        list[modj] = tmp
        i += 1
        j -= 1

def run(input):
    lengths = [int(n) for n in input.split(',')]
    current_position = 0
    skip_size = 0
    hash(lengths, current_position, skip_size)
    return list[0]*list[1]

def hash(lengths, current_position, skip_size):
    for length in lengths:
        reverse(list, current_position, length)
        current_position += length + skip_size
        skip_size += 1

    return current_position, skip_size

def main():
    new_input = raw_input("> ")
    if new_input:
        global list
        list = range(5)
        print run(new_input)
    else:
        print run(input)

if __name__ == '__main__':
    main()
