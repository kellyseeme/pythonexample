#!/usr/bin/env python
def foo():
    a =1
    def bar():
        a = a +1
        return a
    return bar

c = foo()
print c()
