#!/usr/bin/env python

from multiprocessing import Pipe,Process

class Pool(object):
    @classmethod 
    def spawn(cls,f):
        def fun(pipe,x):
            pipe.send(f(x))
            pipe.close()
        return fun

    @classmethod
    def partmap(cls,f,X):
        pipe = [Pipe() for x in X]
        proc = [Process(target=cls.spawn(f),args=(c,x)) for x,(p,c) in zip(X,pipe)]
        [p.start() for p in proc]
        [p.join() for p in proc]
        return [p.recv() for p,m in pipe]

def kel(x):
    return 'hello,',x

print Pool.partmap(kel,['kel','smile'])
