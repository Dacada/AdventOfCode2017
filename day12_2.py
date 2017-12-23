#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import day12

class Day(day12.Day):
    def run(self, programs):
        count = 0
        seen = set()
    
        for group in programs:
            if group not in seen:
                empty = True
                for program in programs:
                    if program not in seen:
                        if programs[program].connects_to(group):
                            seen.add(program)
                            empty = False
                if not empty:
                    count += 1
                
        return count

if __name__ == '__main__':
    Day(12).main()
