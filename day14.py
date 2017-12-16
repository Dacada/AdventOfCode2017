#!/usr/bin/python
# -*- encoding:utf-8 -*-

import day10_2

input = "hwlqcszp"

def run(input):
    count = 0
    
    for i in range(128):
        hash_input = input + '-' + str(i)
        hash = day10_2.run(hash_input)
        count += len([c for c in bin(int(hash,16)) if c == '1'])
        day10_2.day10.list = range(256)
                
    return count

def main():
    new_input = raw_input("> ")
    if new_input:
        print run(new_input)
    else:
        print run(input)

if __name__ == '__main__':
    main()
