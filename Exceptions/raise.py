#!/usr/bin/python3
"""
    The Script runs a Module that raises exceptions
"""
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('ZeroDivision is Prohibited')
    return a / b
try:
    result = divide(17, 0)
except ValueError:
    print("Integers Please")

