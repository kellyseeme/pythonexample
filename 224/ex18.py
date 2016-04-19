#!/usr/bin/env python
from sys import argv
from os.path import exists

script,from_file,to_file = argv

in_file,indate = open(from_file),open(from_file).read()

print """
    Copying from %s to %s " 
    "The input file is %d bytes long"  
    "Does the output file exist? %r " 
    "Ready,hit RETURN to continue,CTRL-C to abort."
""" % (from_file,to_file,len(indate),exists(to_file))
raw_input()

out_file = open(to_file,"w")
out_file.write(indate)

print "Alright,all done"

out_file.close()
in_file.close()

