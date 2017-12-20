#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import base

class Coord(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self._total = None

    def total(self):
        if self._total is None:
            self._total = abs(self.x) + abs(self.y) + abs(self.z)
        return self._total

class Particle(object):
    def __init__(self, p, v, a):
        self.p = Coord(*p)
        self.v = Coord(*v)
        self.a = Coord(*a)

    def total_a(self):
        return self.a.total()
    def total_v(self):
        return self.v.total()
    def total_p(self):
        return self.p.total()

class Day(base.Base):
    def parse(self, input):
        result = []
        for line in input.split('\n'):
            if line:
                sep = line.split(',')
                l = []
                for i in range(3):
                    x = int(sep[i*3][sep[i*3].index('<')+1:])
                    y = int(sep[i*3+1])
                    z = int(sep[i*3+2][:-1])
                    l.append((x,y,z))
                result.append(Particle(*l))
        return result
        
    def run(self, input):
        min_particle = input[0]
        for particle in input[1:]:
            if particle.total_a() < min_particle.total_a():
                min_particle = particle
            elif particle.total_a() == min_particle.total_a():
                if particle.total_v() < min_particle.total_v():
                    min_particle = particle
                elif particle.total_v() == min_particle.total_v():
                    if particle.total_p() < min_particle.total_p():
                        min_particle = particle
        return input.index(min_particle)

if __name__ == '__main__':
    Day(20).main()
