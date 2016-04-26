#!/usr/bin/env python
class cartesianPoint(object):
    pass
cp1 = cartesianPoint()
cp2 = cartesianPoint()
cp1.x = 1.0
cp1.y = 2.0
cp2.x = 1.0
cp2.y = 3.0
def samePoint(p1,p2):
    return (p1.x == p2.x) and (p1.y == p2.y)
def printPoint(p):
    print 'x:',p.x,'y:',p.y

print cp1.x,cp1.y,cp2.x,cp2.y
print samePoint(cp1,cp2)
print cp1 is cp2
printPoint(cp1)
printPoint(cp2)
