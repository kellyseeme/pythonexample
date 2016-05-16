#!/usr/bin/env python

import os.path
import time
#while os.path.getsize('messages') <1000000000:
#    f = open('messages','a')
#    f.write('this is a file/n')
#    f.close()

#print 'file create complted'

#22s
start_time = time.time()
f = open('messages','r')
for i in f:
    end_time = time.time()
    print end_time - start_time
    break
f.close()

#22s
start_time = time.time()
f = open('messages','r')
for i in f.xreadlines():
    end_time = time.time()
    print end_time - start_time
    break
f.close()


start_time = time.time()
f = open('messages','r')
k= f.readlines()
f.close()
end_time = time.time()
print end_time - start_time
