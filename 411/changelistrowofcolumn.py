#!/usr/bin/env python
'''
this is for to use the list of row to the columns
'''

#define a list
arr = [[1,2,3],[4,5,6]]
print [[r[col] for col in (1,0)] for r in arr]

print 'another way to do this'

print [[row[ci] for ci in (1,0)] for row in arr]

print 'there is a way of change the row to the colum'

print [[r[col] for r in arr] for col in range(len(arr[0]))]

def pick_and_reorder_columns(listOfRows,column_indexes):
    return [[row[ci] for ci in column_indexes] for row in listOfRows]

print pick_and_reorder_columns(arr,(0,1))
