#!/usr/bin/env python
"""
this is for the dictionary test

this place is used the list to the dictionary,and find the key and value in the dictionary
"""
contact_dic = {}
with open("kelly") as f:
    for i in f.readlines():
        line = i.strip().split(" ")
        contact_dic[line[0]] = line[1:]
keywords = raw_input("What user infomation your want to get :")
value = contact_dic.get(keywords) 
if value is not None:
    print "this person's phone number is %s,the email address is %s" % (value[0],value[1])
else:
    for name,values in contact_dic.items():
        if name.count(keywords) != 0:
           print name,values
        for i in values:
            if i.count(keywords):
                print name,values
#    else: 
#        print "this is not this person"
