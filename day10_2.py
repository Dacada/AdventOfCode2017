#!/usr/bin/python
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

def run(input):
    lengths = [ord(c) for c in input.strip()]
    lengths.extend((17, 31, 73, 47, 23))
    current_position = 0
    skip_size = 0
    for __ in range(64):
        current_position,skip_size = day10.hash(lengths, current_position, skip_size)
    return finish_hash(day10.list)
    
def main():
    new_input = raw_input("> ")
    if new_input:
        print run(new_input)
    else:
        print run(day10.input)

if __name__ == "__main__":
    main()
