#!/usr/bin/python

#Make a list
somecolours=['red','orange','yellow', 'green', 'blue', 'purple']
print("First colour", somecolours[0])
print("first 2 colours", somecolours[:2])
print("last colour", somecolours[-1])
print("second to last colour", somecolours[-2])

print(set(somecolours))

somecolours2 = ['blue','green','red','green']
print("new list: ", somecolours2)
print("how many green", somecolours2.count('green'))
print("position of first occurance of green", somecolours2.index('green'))

