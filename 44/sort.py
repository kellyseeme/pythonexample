#!/usr/bin/env python

#using key word of cmp
#the cmp function must have two arguments,and the arguments is the iterable item
def cmp_value(x,y):
    if x > y : 
        return 1
    elif x < y:
        return -1
    else:
        return 0
so = sorted('this is a string'.split(' '),cmp=cmp_value)
print so

#using key word of key
so = sorted('this Is a string'.split(' '),key=str.upper)
print so

so = sorted('This is a string'.split(' '),key=lambda x:x.lower)
print so

student = [('kel','C',30),('jun','A',25)]
so = sorted(student,key=lambda x:x[2])
print so

class Student(object):
    def __init__(self,name,score,age):
        self.name = name
        self.score = score
        self.age = age
    def __repr__(self):
        return repr((self.name,self.score,self.age))
student_some = [Student('kel','B',35),Student('jun','C',30)]
print sorted(student_some,key= lambda x :x.age)
