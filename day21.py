#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import base

class Day(base.Base):
    def parse(self, input):
        image = Image('.#./..#/###')
        for enhancment in input.split('\n'):
            s = enhancement.split('=>')
            image.rule(s[0].strip(), s[1].strip())
        return image
        
    def run(self, image):
        for __ in range(5):
            image.improve
        return str(image)

if __name__ == '__main__':
    Day(0).main()
