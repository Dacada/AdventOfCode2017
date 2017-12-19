#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import day1

class Day(day1.Day):
    def run(self, input):
        sum = 0
        step = int(len(input)/2)
        circular_list = input + input
        for i in range(len(input)):
            if circular_list[i] == circular_list[i+step]:
                sum += circular_list[i]
        return sum

if __name__ == '__main__':
    Day(1).main()
