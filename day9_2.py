#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import day9

class Day(day9.Day):
    def parse(self,input):
        return input
    
    def run(self, input):
        input = input.strip()
        assert input[0] == '{' and input[-1] == '}'
        input = input[1:-1]
    
        stack = [[]]
        state = 'read'

        count = 0
    
        for c in input:
            if state == 'read':
                if c == '{':
                    stack.append([])
                elif c == '}':
                    current_group = stack.pop()
                    stack[-1].append(current_group)
                elif c == '<':
                    state = 'garbage'
            elif state == 'garbage':
                if c == '>':
                    state = 'read'
                elif c == '!':
                    state = 'ignore'
                else:
                    count += 1
            elif state == 'ignore':
                state = 'garbage'

        return count

if __name__ == '__main__':
    Day(9).main()
