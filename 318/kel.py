#!/usr/bin/env python
from multiprocessing import Pool
class calculate(object):
    def run(self):
        def f(x):
            return x*x
        p = Pool()
        return p.map(f,[1,2,3]) 

c1 = calculate()
print c1.run()
