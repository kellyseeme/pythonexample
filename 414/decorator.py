#!/usr/bin/env python
def make_filter(keep):
    def the_filter(file_name):
        file = open(file_name)
        lines = file.readlines()
        file.close()
        filter_doc = [i for i in lines if keep in i]
        return filter_doc
    return the_filter

filter=make_filter('pass')
print filter('result.txt')
filter=make_filter('this')
print filter('result.txt')
