#!/usr/bin/python3
# -*- encoding:utf-8 -*-

import math
import base

def is_prime(n):
    limit = int( math.ceil( math.sqrt(n) ) )
    for i in range(2,limit+1):
        if n % i == 0:
            return False
    return True
            
class Day(base.Base):
    """
    The input assembly is trying to tell how many composite numbers
    exist between 100081 and 117081 in increments of 17.
    
    Let's answer this question. And for added fun lets take the actual
    numbers from the input file.
    """
    def parse(self, input):
        lines = [l for l in input.split('\n') if l]
        _,__,a = lines[0].split()
        _,__,b = lines[4].split()
        _,__,c = lines[5].split()
        frm = int(a)*int(b)-int(c)
        _,__,d = lines[7].split()
        to = frm-int(d)
        _,__,e = lines[-2].split()
        stp = -int(e)
        return (frm,to,stp)
        
    def run(self, input):
        frm,to,stp = input
        return len([n for n in range(frm, to+1, stp) if not is_prime(n)])
        

if __name__ == '__main__':
    Day(23).main()
