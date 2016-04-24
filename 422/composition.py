#!/usr/bin/env python
class Phone(object):
    def __init__(self,ph):
        self.phone = ph

class Person(object):
    def __init__(self,nm,ph):
        self.name = nm
        self.phone = Phone(ph)

class Kel(Person):
    def shout(self):
        pass

