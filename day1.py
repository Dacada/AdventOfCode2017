#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import base

class Day(base.Base):
    def parse(self, input):
        return [int(c) for c in input.strip()]
        
    def run(self, input):
        sum = 0
        
        for i in range(len(input)-1):
            if input[i] == input[i+1]:
                sum += input[i]
                
        if input[-1] == input[0]:
            sum += input[0]
            
        return sum

if __name__ == '__main__':
    Day(1).main()
