#!/usr/bin/python
# -*- encoding:utf-8 -*-

import day1

def run(input):
    input_list = [int(c) for c in input]
    sum = 0
    step = len(input_list)/2
    circular_list = input_list + input_list
    for i in range(len(input_list)):
        if circular_list[i] == circular_list[i+step]:
            sum += circular_list[i]
    return sum

day1.run = run

if __name__ == '__main__':
    day1.main()
