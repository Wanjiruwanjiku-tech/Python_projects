#!/usr/bin/python3
"""
    This Script runs a Module that handles exceptions
"""
#FileNotFound Error
try:
    file = open("non_existent_file.txt", "r")
except FileNotFoundError:
    print("Error: file not found")

#KeyError
try:
    my_dict = {"girls" : 4, "boys" : 5}
    for key, value in my_dict.items():
        print(key, value)

    print(my_dict['man'])
except KeyError:
    print("Error: Key not found")

#IndexError
try:
    mylist = [1, 3, 5, 7, 9]
    print(mylist)
    print(mylist[8])
except IndexError:
    print("Error: index out of range")
