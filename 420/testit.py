#!/usr/bin/env python
#'this is a example of the unit test'
def testit(func,*nkwargs,**kwargs):
    'this is the test of the function'
    try:
        retval = func(*nkwargs,**kwargs)
        result = (True,retval)
    except Exception,diag:
        result = (False,str(diag))
    return result

def main():
    'this is the unittest input'
    funcs = (int,long,float)
    vars = (12,12.34,'12','12.34')
    for eachFunc in funcs:
        print '-'*20
        for eachVal in vars:
            result = testit(eachFunc,eachVal)
            if result[0]:
                print '%s(%s) = ' % (eachFunc.__name__,eachVal),result[1]
            else:
                print '%s(%s) FAILED:' % (eachFunc.__name__,eachVal),result[1]

if __name__== '__main__':
    main()
