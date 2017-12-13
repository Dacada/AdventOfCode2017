#!/usr/bin/python
# -*- encoding:utf-8 -*-

import day8

class RegisterBank(object):
    def __init__(self):
        self._registers = {}
        self._max = 0

    def get(self, register_name):
        if register_name not in self._registers:
            self._registers[register_name] = 0
        return self._registers[register_name]

    def set(self, register_name, value):
        self._registers[register_name] = value
        if value > self._max:
            self._max = value

    def max(self):
        return self._max

day8.RegisterBank = RegisterBank

if __name__ == '__main__':
    day8.main()
