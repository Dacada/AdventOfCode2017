#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import base

class Day(base.Base):
    def is_valid(self, sentence):
        words = sentence.split()
        s = set()
        for word in words:
            if word in s:
                return False
            s.add(word)
        return True
    
    def parse(self, input):
        return [s for s in input.split('\n') if s]
    
    def run(self, input):
        count = 0
        for sentence in input:
            if self.is_valid(sentence):
                count += 1
        return count

if __name__ == "__main__":
    Day(4).main()
