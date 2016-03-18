#/usr/bin/env python
from multiprocessing import Pool

p = Pool(5)
def kel(x):
     return x*x
"""
if __name__ == "__main__":
    p = Pool(5)
    print p.map(kel, [1,2,3])
"""
#p = Pool(5)
print p.map(kel, [1,2,3])
