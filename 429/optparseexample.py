#!/usr/bin/env python

from optparse import OptionParser

usage = 'usage:%prog [options] arg'
parser = OptionParser(usage)
parser.add_option('-f','--file',dest='filename',
                  help='write report to FILE',metavar='FILE')
parser.add_option('-q','--quite',
                  action='store_false',dest='verbose',default=True,
                  help="'don't print status messages to  stdout")
#args = ['kel']
(options,args) = parser.parse_args()
print options
print args
