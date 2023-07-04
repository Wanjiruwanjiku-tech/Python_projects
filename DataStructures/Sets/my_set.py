#!/usr/bin/python3
"""
    THIS MODULE GIVES EXPLANATION ON SETS
"""

set1 = set([1, 2, 3, 4])
set2 = {4, 5, 6, 7}

print("Hi I am Set, I am an Unordered Collection of items that are mutable\n")
print("The most unique thing about me is that 'I DO NOT ACCEPT DUPLICATES\n'")
print("This is me: {}, and this is my friend: {}".format(set1, set2))
print()
print("\tBASIC SET OPERATIONS\n")
print("1. UNION")
print("First Set: {}, Second Set: {}".format(set1, set2))
print(set1.union(set2))
print()
print("2. INTERSECTION")
print(set1&set2)
print()
print("3. DIFFERENCE")
print(set1.difference(set2))
mylist = [1, 1, 3, 5, 6, 7, 7, 8, 8, 9, 8, 9, 1, 2, 4, 4]
set3 = set(mylist)
print("List with Duplicates: {}".format(mylist))
print("Unique items in the list above: {}".format(set3))

