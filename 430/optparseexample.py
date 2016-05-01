#!/usr/bin/env python

from optparse import OptionParser

usage = 'this is the method of the script'
parser = OptionParser(usage)
parser.add_option('-f','--file',dest='filename'
                  ,help='this is the filename')
parser.add_option('-n',type='int',dest='num')
args = ['-fkel','-n42']
(options,args) = parser.parse_args(args)
print 'the options.filename is : ',options.filename,options.num
print args
