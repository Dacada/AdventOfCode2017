#!/usr/bin/python
# -*- encoding:utf-8 -*-

input = '18,1,0,161,255,137,254,252,14,95,165,33,181,168,2,188'
list = range(256)

def reverse(list, start, length):
    """
    Reverse a slice of the given list in place. The slice is defined by the starting index and the total length. Wrap back to the start if end of list is reached.
    """
    

def run(input):
    lengths = [int(n) for n in input.split(',')]
    current_position = 0
    skip_size = 0

    for length in lengths:
        reverse(list, current_position, length)
        current_position += length + skip_size
        skip_size += 1

    return list[0]*list[1]

def main():
    new_input = raw_input("> ")
    if new_input:
        list = range(5)
        run(new_input)
    else:
        run(input)

if __name__ == '__main__':
    main()
