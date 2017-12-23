#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import base

def score(group, acc):
    return 1 + acc + sum(score(g, acc+1) for g in group)

class Day(base.Base):
    def parse(self, input):
        input = input.strip()
        assert input[0] == '{' and input[-1] == '}'
        input = input[1:-1]
    
        stack = [[]]
        state = 'read'
    
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
            elif state == 'ignore':
                state = 'garbage'

        return stack.pop()

    def run(self, groups):
        return score(groups, 0)

if __name__ == "__main__":
    Day(9).main()
