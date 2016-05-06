#!/usr/bin/env python

from multiprocessing import Pool


class calculate(object):
    def run(self):
        def fun(x):
            return x*x
        p = Pool()
        return p.map(fun,[1,2,3])


c1 =calculate()
print c1.run()

