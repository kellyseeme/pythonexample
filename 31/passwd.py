#!/usr/bin/env python
"""
this is for a user login program
"""

def checkNameAndPassword(name,password):
    "this is for the user login ,return the status"
#open the user name and password file,get the username and user password
    fobj = open("username.txt")
#this is for the user login stat,return this value
    loginstat = 0 
#this is to get all the username and the passrod
    for line in fobj:
#put the username and password in a list
        lineList = line.strip().split(" ")
#check the user name and password is correct?
        if name == lineList[0] and password ==lineList[1]:
#this is correct,then retun the status 1,can login
            loginstat = 1
            break
#this is the name is wright,but the password is incorrect
        elif name == lineList[0]: 
            loginstat = 2
            break
        else:
#this is the user not in the system
            loginstat = 3
    fobj.close()
#return the user status
    return loginstat    

def getLockuser():
    "this is get the lock user name"
#this is open the lock file,get the locked user name
    fobj = open("lock.txt")
    userList = []
    for f in fobj:
        userList.append(f.strip())
    return userList

#this is to check the how many times is to retry
loginTime = 0
#this is to check to enter the user name again
namePass = True

while loginTime < 3:
    if namePass:
        username = raw_input("Enter your name:")
    if username in getLockuser():
        print "SB,OUT"
        break
    userpasswd = raw_input("Enter your password:")
    if len(username) == 0 and len(userpasswd) ==0:
       print "login existed!!!"
       break
    login = checkNameAndPassword(username,userpasswd)

    if login == 1:
        print "Welcome to the system"
        break
    elif login == 2:
        print "password is incrrect"
        namePass = False
    else:
        print "the user is not in the system"
    if login == 2 and loginTime ==2:
        fobj = open("lock.txt","a")
        fobj.write(username+"\n")
        fobj.close()
    loginTime += 1
