#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import day10

def xor(list):
    r = list[0]
    for i in range(1,len(list)):
        r ^= list[i]
    return r

def finish_hash(list):
    result = ""
    for i in range(16):
        dense = xor(list[i*16:(i+1)*16])
        result += hex(dense|0x100)[3:]
    return result

class Day(day10.Day):
    def parse(self, input):
        return [ord(c) for c in input.strip()]
    
    def run(self, lengths):
        lengths.extend((17, 31, 73, 47, 23))
        current_position = 0
        skip_size = 0
        for __ in range(64):
            current_position,skip_size = self.hash(lengths, current_position, skip_size)
        return finish_hash(self.list)

if __name__ == "__main__":
    Day(10).main()
