#!/usr/bin/python
# -*- encoding:utf-8 -*-

import copy
import day13

class Layer(day13.Layer):
    def tick_many(self, ticks):
        mod = self.range - 1
        mod2 = mod * 2
        
        self.current = ticks % mod2
        if self.current >= self.range:
            self.current = mod2 - self.current
            
        self.direction = +1 if (ticks / mod) % 2 == 0 else -1
        if self.current == 0:
            self.direction = -1
        if self.current == self.range - 1:
            self.direction = 1

day13.Layer = Layer

class Firewall(day13.Firewall):
    def __init__(self, definition):
        self.delay = 0
        super(Firewall, self).__init__(definition)

    def reset(self):
        self.player_position = 0
        for layer in self._layers.values():
            layer.current = 0
            layer.direction = -1

    def tick_many(self, ticks):
        for layer in self._layers.values():
            layer.tick_many(ticks)

    def perfect_run(self):
        self.tick_many(self.delay)
        
        end = max(self._layers)
        while self.player_position <= end:
            if self.player_caught():
                return False
            self.tick()
            
        return True

    def __repr__(self):
        r = ""
        for l in self._layers.values():
            r += repr(l)
            r += '\n'
        return r
        
day13.Firewall = Firewall

def run(input):
    firewall = day13.parse(input)
    delay = 0
    while True:
        delay += 1
        firewall.reset()
        firewall.delay = delay
        if firewall.perfect_run():
            return delay

day13.run = run

if __name__ == '__main__':
    day13.main()
