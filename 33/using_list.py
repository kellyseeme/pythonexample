#!/usr/bin/env python
"""
this is for test the list function
"""
#this is define the shoplist of a list
shoplist = ["apple","mango","carrot","banana"]

#get the shoplist length,using len(shoplist)
print "Ihave",len(shoplist),"items to pruchase."

#this is iteration of the list,the list is iterable
print "These items are:",
for item in shoplist:
#there have a comma at the end of the line,it's mean is ride of the newline
    print item,

print "\nIalso have to buy rice."
#this is append the function,add a shopinglinst a rice,using append
#append is the last the argument
shoplist.append("rice")
print "My shopping list is now",shoplist

print "I will sort my list now"
#list is a changeable,so this is sort,and the list is changed
shoplist.sort()
print "Sorted shoping list is ",shoplist

print "The first item I will buy is ",shoplist[0]
#this is get the list of value,use the index and then get the value
olditem = shoplist[0]
#this is delete some of the list
del shoplist[0]
print "I bouthe the",olditem

print "My shopping list is now",shoplist
