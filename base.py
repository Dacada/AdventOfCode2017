#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import os
import time
import pickle
import requests

class Base(object):
    def __init__(self, day, test=False):
        self.timer = None
        self.day = day
        self.test = test
        if test:
            self.cookie = None
        else:
            with open('session.pkl', 'rb') as f:
                self.cookie = pickle.load(f)

    def fetch(self):
        if self.test:
            return self._load('test' + str(self.day) + '.txt')
        else:
            filename = 'input' + str(self.day) + '.txt'
            url = 'http://adventofcode.com/2017/day/' + str(self.day) + '/input'
        
            if not os.path.isfile(filename):
                self._fetch_url(url, filename)

            return self._load(filename)

    def _fetch_url(self, url, filename):
        r = requests.get(url, cookies=self.cookie)
        r.raise_for_status()
        with open(filename, 'w') as f:
            f.write(r.text)

    def _load(self, filename):
        with open(filename) as f:
            return f.read()

    def parse(self, input):
        raise NotImplementedError

    def run(self, input):
        raise NotImplementedError

    def time_start(self):
        self.timer = time.time()

    def time_stop(self):
        return time.time() - self.timer

    def output(self, result, time_passed):
        print("Day", self.day)
        print("Result:", result)
        print("Time elapsed:", time_passed)
        
    def main(self):
        input = self.fetch()
        parsed_input = self.parse(input)
        
        self.time_start()
        result = self.run(parsed_input)
        time_passed = self.time_stop()
        
        self.output(result, time_passed)
