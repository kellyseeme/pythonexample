#!/usr/bin/env python
from sys import argv
from os.path import exists

script,from_file,to_file = argv
in_file = open(from_file)
out_file = open(to_file,"w")
indata = in_file.read()
print """
	Copying file %s to %s.
	The imput file is %d bytes long.
	the output file is exists? %s
	Ready,hit RETURN to continue,CTRL-C to abort
""" % (from_file,to_file,len(indata),exists(to_file))
raw_input("?")
out_file.write(indata)

print "All is done"
in_file.close()
out_file.close()
