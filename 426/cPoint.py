#!/usr/bin/env python
import math
class cPoint(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.radius = math.sqrt(self.x*self.x+self.y*self.y)
        self.angle = math.atan2(self.y,self.x)
    def cartesian(self):
        return (self.x,self.y)
    def polar(self):
        return (self.radius,self.angle)
    def __str__(self):
        return str(self.x) + str(self.y)
    def __cmp__(self,other):
        return (self.x > other.x) and (self.y >other.y)
