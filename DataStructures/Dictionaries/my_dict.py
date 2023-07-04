#!/usr/bin/python3
"""
    The script Defines a dictionaey
"""
print("Hi, I am Dictionary, I am also an example of a data structure in Python\n")
print("Guys say I am a Collection of unordered key-value pairs, where each key is unique\n")
print("My other Names are 'ASSOCIATIVE ARRAYS' and 'HASH MAPS'\n")
my_example = {"apples" : 3, "bananas" : 4, "mangoes": 5, "fruits": "I love my Fruits"}
print("This is Me: {}".format(my_example))
print("My Values")
print(my_example['fruits'])
print(my_example['bananas'])
print(my_example['mangoes'])
print(my_example['apples'])
print(my_example.get('apple')) #Using get() Method
#Returns None if key is non-existant
print("\nAdding a new Fruit\n")
my_copy = my_example
my_copy["grapes"] = 5
print("Original: {}\n".format(my_example))
print("Added Fruit: {}\n".format(my_copy))
print()
for keys in my_copy:
    print("My Key: \n", keys)
    print()
for key, value in my_copy.items():
    print('Both Keys: {} and Values: {}'.format(key, value))
