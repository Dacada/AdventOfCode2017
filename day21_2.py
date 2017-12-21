#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import day21

class Day(day21.Day):
    def run(self, art):
        for __ in range(18):
            art.improve()
        return count_char(str(art),'#')

if __name__ == '__main__':
    Day(21).main()
