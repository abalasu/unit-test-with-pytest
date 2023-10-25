import math
import numpy 
import ctypes


def mod_7(x):
    """Return the remainder of x after dividing by 7"""
    return x % 7

print(
    'Which number is biggest?',
    max(100, 51, 14),
    'Which number has the biggest modulo 7?',
    max(100, 52, 14, key=mod_7),
    sep='\n',
)

# print(dir(math))
# print(math.__doc__)
help(mod_7)
# print(dir(numpy))
# print(dir(ctypes))