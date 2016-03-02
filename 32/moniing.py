#!/usr/bin/env python
"""
this is for change the file content

if we will change the file content,we must read it all,and then install the content in the file
"""
f = open("kel","w+")
for i in range(1,20):
    f.write("loop times "+ str(i) +" \n")
f.seek(0)
f.flush()
lineList = f.readlines()
f.close()

f = open("kel","w")
lineList[10] = "this is the new one\n"
f.writelines(lineList)
f.close()

f = open("kel")
for i in f:
    print i,
f.close()
