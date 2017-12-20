#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import base

class Day(base.Base):
    def parse(self, input):
        return [[int(num) for num in row.split() if num] for row in input.split('\n') if row]

    def run(self, input):
        checksum = 0

        for row in input_table:
            checksum += max(row) - min(row)

        return checksum

if __name__ == "__main__":
    Day(2).main()
