#!/usr/bin/env python
'''
this is get the file longest line
'''
import time
#start_time = time.time()
#lo = max((len(line) for line in open('kel.log') ))
#print lo
#end_time = time.time()
#print end_time-start_time
start_time = time.time()
lo = max([len(line) for line in open('kel.log') ])
print lo
end_time = time.time()
print end_time-start_time
