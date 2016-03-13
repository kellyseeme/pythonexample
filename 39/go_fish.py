#!/usr/bin/env python
import random
all_list = [1,2,3,4,5,6,7,8,9,10,11,12,13]*3

father = []
girl = []


def getcard(num,who):
    i = 0
    while i < num:
        m = random.randint(1,13)
        all_list.pop(m)
        who.append(m)
        i = i + 1
while len(all_list) > 0:
    getcard(5,father)
    getcard(5,girl)
    m = father.count()
