#!/usr/bin/env python

class HotelRoomCalc(object):
    'Hotel room rate claculator'
    
    version = 1.0
    
    def testClassAttribute(self):
        print HotelRoomCalc.version
        version = 3.1
        print version
        print HotelRoomCalc.version
        HotelRoomCalc.version += 1
        print HotelRoomCalc.version


    def __init__(self,rt,sales=0.085,rm=0.1):
        'HotelRoomCalc default arguments:sales and rm'
        self.salesTax = sales
        self.roomTax = rm
        self.roomRate = rt
        self._kel = 'private'

    def clacToral(self,days=1):
        'Calculate total:default to daily rate'
        daily = round((self.roomRate * 14 * (1 + self.roomTax + self.salesTax)),2)
        return float(days) * daily

sfo = HotelRoomCalc(299)
sfo.testClassAttribute()
#print HotelRoomCalc.__dict__
#print sfo.clacToral()
#print sfo.clacToral(2)
