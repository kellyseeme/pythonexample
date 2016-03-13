#!/usr/bin/env python
"""
this is for the dicitonary test

this is two diction to store the cities and the state of the abbreviation
"""
#create a mapping of state to abbreviation
#this is the dictionary to store the state of abbreviation
states = {
    "Oregon":"OR",
    "Florida":"FL",
    "California":"CA",
    "New York":"NY",
    "Michigan":"MI"
}

#create a basic set of states and some cities in them
cities = {
    "CA":"San Francisco",
    "MI":"Detroit",
    "FL":"Jacksonville"
}

#add some more cities
cities["NY"] = "New York"
cities["OR"] = "Portland"

#print out some cities
print "-"*10
print "NY State has: ",cities["NY"]
print "OR State has: ",cities["OR"]

#print some states
print "-"*10
print "Michigan's abbreviation is : ",states["Michigan"]
print "Florida's abbreviation is : ",states["Florida"]

#do it by using the state then cities dict
print "-"*10
print "-"*10
print "Michigan has: ",cities[states["Michigan"]]
print "Florida has: ",cities[states["Florida"]]

#print every state abbreciation
#this is to get the loop,use loop this is use the the diction of items()
#this diction items will return the keys and values,so this is for print
print "-"*10
for state,abbrev in states.items():
    print "%s has the city %s" % (state,abbrev)

#print every city in state
print "-"*10
for abbrev,city in cities.items():
    print "%s has the city %s " % (abbrev,city)

#now do both at the same time
print "-"*10
for state,abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" %(state,abbrev,cities[abbrev])

print "-"*10
#safely get a abbreviation by state that might not be there
#this is for to get the values,if this keys to find,and the values is not exist ,then will retun None,
#this get is the safry get values,keys and values is the items
state = states.get("Texas")

if not state:
   print "Sorry,no Texas."

#get a city with a default value
#the get function can be used to set the default value,if this is not find the keys ,then 
#return the deault values
city = cities.get("TX","Does Not Exist")
print "The city for the state 'TX' is : %s" % city
