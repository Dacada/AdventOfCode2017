#!/usr/bin/python
# -*- encoding:utf-8 -*-

import day2

def find_divisible(l):
    for a in l:
        for b in l:
            if a != b:
                if a % b == 0:
                    return a,b
                elif b % a == 0:
                    return b,a
    return None,None

class Day(day2.Day):
    def run(input):
        checksum = 0

        for row in input_table:
            a,b = find_divisible(row)
            checksum += a/b

        return checksum

if __name__ == '__main__':
    Day(2).main()
