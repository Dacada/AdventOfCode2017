#!/usr/bin/python
# -*- encoding:utf-8 -*-

import day19

class CountingRouter(day19.Router):
    def __init__(self, grid):
        super(CountingRouter, self).__init__(grid)
        self.step_count = 1

    def advance(self, direction):
        super(CountingRouter, self).advance(direction)
        self.step_count += 1

def run(input):
    router = CountingRouter(open(input).read())
    router.traverse()
    return router.step_count
day19.run = run

if __name__ == "__main__":
    day19.main()
