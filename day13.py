#!/usr/bin/python
# -*- encoding:utf-8 -*-

import sys

input = """0: 3
1: 2
2: 4
4: 4
6: 5
8: 8
10: 6
12: 6
14: 6
16: 6
18: 8
20: 8
22: 12
24: 10
26: 9
28: 8
30: 8
32: 12
34: 12
36: 12
38: 12
40: 8
42: 12
44: 14
46: 14
48: 10
50: 12
52: 12
54: 14
56: 14
58: 14
62: 12
64: 14
66: 14
68: 14
70: 12
74: 14
76: 14
78: 14
80: 18
82: 17
84: 30
88: 14"""

class Layer(object):
    def __init__(self, range):
        self.range = range
        self.current = 0

    def tick(self):
        self.current += 1
        if self.current == self.range:
            self.current = 0

class Firewall(object):
    def __init__(self, definition):
        self._layers = {}
        for i in definition:
            self._layers[i] = Layer(definition[i])
        self.player_position = 0

    def player_caught(self):
        return self.player_position in self._layers and self._layers[self.player_position] == 0

    def get_severity(self):
        return self.player_position * self._layers[self.player_position].range

    def tick(self):
        self.player_position += 1
        for layer in self._layers.values():
            layer.tick()

    def run(self):
        end = max(self._layers)
        severity = 0
        
        while self.player_position <= end:
            if self.player_caught():
                severity += self.get_severity()
            self.tick()

        return severity

def parse(input):
    d = {}
    for line in input.split('\n'):
        if line:
            layer,range = line.split(':')
            d[int(layer)] = int(range.strip())
    return Firewall(d)

def run(input):
    firewall = parse(input)
    return firewall.run()

def main():
    sys.stdout.write("> ")
    new_input = sys.stdin.read()
    if new_input:
        print run(new_input)
    else:
        print run(input)

if __name__ == '__main__':
    main()
