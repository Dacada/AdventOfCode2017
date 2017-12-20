#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import day20

class System(object):
    def __init__(self, particles):
        self._particles = {}
        for i,p in enumerate(particles):
            self._particles[i] = p

    def tick(self):
        match = {}
        for name,particle in self._particles.items():
            key = (particle.p.x, particle.p.y, particle.p.z)
            if key in match:
                match[key].append(name)
            else:
                match[key] = [name]

            _tick_particle(particle)
            
        for names in match.values():
            if len(names) > 1:
                for name in names:
                    del self._particles[name]

        return len(self._particles)


def _tick_particle(particle):
    #Too lazy to override particle amd have to copy paste parse.
    particle.v.x += particle.a.x
    particle.v.y += particle.a.y
    particle.v.z += particle.a.z
    particle.p.x += particle.v.x
    particle.p.y += particle.v.y
    particle.p.z += particle.v.z

class Day(day20.Day):
    def parse(self, input):
        l = super(Day, self).parse(input)
        return System(l)
        
    def run(self, input):
        for i in range(50):
            n = input.tick()
        return n
        

if __name__ == '__main__':
    Day(20).main()
