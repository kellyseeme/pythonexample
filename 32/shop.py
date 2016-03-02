#!/usr/bin/env python

score = raw_input("Enter your money:")
shoppingList = ["fruits","origin","bottle"]
priceList = [8.42,10,20]

prompt = """
    this is the shopping list,please enter your choice:
    index , price  
""" 
for m,i in enumerate(zip(shoppingList,priceList)):
    prompt = prompt + "\n    " + str(m+1) + str(i) +"\n    "

money = float(score)
userchoice = 1
while True:
    if money >= priceList[int(userchoice)-1]:
        print prompt
        userchoice = raw_input("what are you want to buy:")
        if userchoice == "q" :
            print "exit the shopping program."
            break
        if int(userchoice) > len(priceList)+1:
            print "your choice is out of the list!"
            continue
        print "your choice is %s" % userchoice
        money = money - priceList[int(userchoice) - 1]
        print "your money is %s" % money
    else:
        print "your money is not enough,%s" % money
        break
        
