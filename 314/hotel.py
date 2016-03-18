#!/usr/bin/env python

class HotelRoomCalc(object):
    "Hotel room rate calculator"

    def __init__(self,rt,sales=0.0085,rm=0.1):
        """Hotel romm calc default arguments"""
        self.salesTax = sales
        self.roomTax = rm
        self.roomRate = rt

    def calcTotal(self,days=1):
        "Calculate total:default to daily rate"
        daily = round((self.roomRate*14*(1+self.roomTax+self.salesTax)),2) 
        return float(days) * daily

kel = HotelRoomCalc(2)
print kel.calcTotal()
