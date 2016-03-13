#!/usr/bin/env python
"""
this is test to define a class
"""
#this is define a class name is Sone,is come from the object class
class Song(object):
    
#this is the creat the clsaa,then add a attribute to the class,this have a prameters
    def __init__(self,lyrics):
#this is to set the parameters to the class,and must use the parameter of self
        self.lyrics = lyrics

#this is to define a function,and use self,this is a function
    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

    def getsong(self):
        print len(self.lyrics)
#this is initiate the class ,and pass it to a variable
happy_baby = Song(["Happy birthday to you",
                  "I dont want to get sued",
                  "So i ll stop right there"])
bulls_on_parade = Song(["Teh relly around tha family",
                        "With pockets full of shells"])

#this is use the create class to call the function of sing_me_a_song()
happy_baby.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

kel_song = Song(["this is the song of the first line",
                     "this is the sone of the second line"])
kel_song.sing_me_a_song()

a_list = ["this is a list","this is a list?"]
so=Song(a_list)
so.sing_me_a_song()
so.getsong()

#this is all the function have the self,this is used to of the class attribute or a local variable,
#so there must have the self keywords
