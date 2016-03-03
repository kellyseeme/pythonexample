#!/usr/bin/env python
"""
this is to test the module of function

1.there is more of function,and the """"""is used to the __doc__,is docstring
2.see the docstring,can use help(ex25)
3.this is a module of name ex25,its used to import
4.the parameter is list,so when you changed the list value in the function,then return the changed value
5.when import a module,the function when it call it will be run,on the import the module,it will not be run
"""
def break_words(stuff):
    """this function will break up words for us."""
    words = stuff.split(" ")
    return words

def sort_words(words):
    """Sorts the words"""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off"""
    word = words.pop(0)
    return word

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of sentence):"""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and the last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

def myowntest():
   "this is my test the __doc__"
   print "this is for test"
