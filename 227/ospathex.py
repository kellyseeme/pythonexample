#!/usr/bin/env python
"""
this is to test the os module 

this is use the os module of attributes and the file
write content and read the content
"""
import os
#this is to get the ttempdir for the special os system
# in the posix system ,is /tmp
#in the windows system,is c:\temp
#if the other system is empty
for tmpdir in ("/tmp",r"c:\temp"):
    if os.path.isdir(tmpdir):
        break
    else:
        print "no temp directory available"
        tmpdir = ""

if tmpdir:
#os.chdir is change the directory
    os.chdir(tmpdir)
#os.getcwd() is get the current work directory
    cwd =os.getcwd()

    print "***current temporary directory"
    print cwd

    print "***creating example directory..."
#os.mkdir is to create a new directory
    os.mkdir("example")
#os.chdir is change to the directory
    os.chdir("example")
    cwd = os.getcwd()

    print "*** new working directory"
    print cwd
    print "***orginal directory listing:"
#os.listdir()is to list the definity direcotry files
    print os.listdir(cwd)

    print "*** createing test file.."
#file is to write some contents
    fobj = open("test","w")
    fobj.write("foo\n")
    fobj.write("bar\n")
    
    print "***renaming test to filetest.txt"
#os.rename is to set the file a new filename
    os.rename("test","filetest.txt")
    print "***updated directory listing:"
    print os.listdir(cwd)
#os.path.join is to concate the current work director and the dir values,and is to get the full path off the file
    path = os.path.join(cwd,os.listdir(cwd)[0])
    print "***full file path name"
    print path

    print "***(pathname,basename) == "
#os.split is split the pathname and the basename
#basename is the filename ,the pathname is the file path
    print os.path.split(path)

    print "***(filename,extentsion)"
#os.splitext is split the path values and the extention
#os.splitext is only to spit the os.path.basename is not of the full file path
    print os.path.splitext(os.path.basename(path))

    print "***displaying file contents"
#this file is used to get the file content
    fobj = open(path)
    for eachLine in fobj:
        print eachLine,
    fobj.close()

    print "***deleteing test file"
#os.remove is deleteing the files
    os.remove(path)
    print "***updated directory listing"
    print os.listdir(cwd)
    os.chdir(os.pardir)

    print "***deleeing test directory"
#os.rmdir is delete the directory
    os.rmdir("example")
    print "***DONE"
