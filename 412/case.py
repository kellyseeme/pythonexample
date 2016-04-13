#!/usr/bin/env python
animals = []
number_of_felines = 0

def deal_with_a_cat():
    global number_of_felines
    print 'meow'
    animals.append('feline')
    number_of_felines += 1

def deal_with_a_dog():
    print 'bar'
    animals.append('canine')

def deal_with_a_bear():
    print 'wathch our for the *HUG*'
    animals.append('usrine')

tokenDICT = {
    'cat':deal_with_a_cat,
    'dog':deal_with_a_dog,
    'bear':deal_with_a_bear,
    }
#simulate,from files to read a word
words = ['cat','bear','cat','dog']
for word in words:
    'find the word method and call it'
    tokenDICT[word]()
nf = number_of_felines
print 'we met %d feline %s ' % (nf,'s'[nf==1:])
print 'the animals we met were:',' '.join(animals)

