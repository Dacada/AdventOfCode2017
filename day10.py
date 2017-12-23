#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import base

def reverse(list, start, length):
    """
    Reverse a slice of the given list in place. The slice is defined
    by the starting index and the total length. Wrap back to the start
    if end of list is reached.
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
            
class Day(base.Base):
    def __init__(self, *args, **kwargs):
        super(Day, self).__init__(*args, **kwargs)
        self.list = [__ for __ in range(256)]

    def parse(self, input):
        return [int(n) for n in input.split(',')]

    def run(self, lengths):
        current_position = 0
        skip_size = 0
        self.hash(lengths, current_position, skip_size)
        return self.list[0]*self.list[1]
    
    def hash(self, lengths, current_position, skip_size):
        for length in lengths:
            reverse(self.list, current_position, length)
            current_position += length + skip_size
            skip_size += 1

        return current_position, skip_size

if __name__ == '__main__':
    Day(10).main()
