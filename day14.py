#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import base
import day10_2

class Day(base.Base):
    def parse(self, input):
        return input.strip()
    
    def run(self, input):
        day = day10_2.Day(14)
        
        count = 0
    
        for i in range(128):
            hash_input = input + '-' + str(i)
            hash = day.run(day.parse(hash_input))
            count += len([c for c in bin(int(hash,16)) if c == '1'])
            day.list = [__ for __ in range(256)]
                
        return count

if __name__ == '__main__':
    Day(14).main()
