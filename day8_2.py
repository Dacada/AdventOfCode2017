#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import day8

class RegisterBank(day8.RegisterBank):
    def __init__(self):
        super(RegisterBank, self).__init__()
        self._max = 0

    def set(self, register_name, value):
        super(RegisterBank, self).set(register_name, value)
        if value > self._max:
            self._max = value

    def max(self):
        return self._max

class Day(day8.Day):
    def run(self, program):
        register_bank = RegisterBank()
        for instruction in program:
            instruction.run(register_bank)
        return register_bank.max()

if __name__ == '__main__':
    Day(8).main()
