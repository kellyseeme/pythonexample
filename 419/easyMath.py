#!/usr/bin/env python

from operator import add,sub
from random import choice,randint

MAXTRIES = 2
op = {'+':add,'-':sub}

def doprobe():
    'use to print the calculate math and the check result'
    nums = [randint(1,10) for i in range(2)]
    nums.sort(reverse=True)
    opera = choice('+-')
    oops = 0
    pr = '%d %s %d ' %(nums[0],opera,nums[1])
    answer = op[opera](*nums)
    ans = '%d %s %d = %d' % (nums[0],opera,nums[1],answer)
    while True:
        try:
            print pr
            userinput = int(raw_input('answer is : '))
            if userinput == answer:
                print 'correct'
                break
            elif oops == MAXTRIES:
                print ans
            else:
                print 'incorrect ,try again'
                oops += 1
        except (KeyboardInterrupt,EOFError,ValueError):
            print 'invalid input ...try again'

def main():
    'this is to sure continue the math'
    while True:
        doprobe()
        try:
            userchoice = raw_input('continue ? [y]/ [n]').lower()
            if userchoice and userchoice[0] == 'n':
                break
        except:
            print 'quit for math'
            break

if __name__ == '__main__':
    main()
