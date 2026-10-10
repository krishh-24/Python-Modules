# Write a function that reverses a string three different ways: slicing, reversed() + join(), and a manual loop. Compare performance using time module for a string of 1 million characters.

import time

# 1. Method 1: Slicing [::-1]

a = "krish"
print(a[::-1])

# a contains "hello".
# [::-1] means read the string backward.
# Python creates a new string: "hsirk".


# Method 2: reversed() + join()

b = "world"
result = " ".join(reversed(b))
print(result)

# reversed(b) reads the characters backward: d, l, r, o, w.
# ''.join(...) combines those characters into one string.
# The result is "dlrow".


# Method 3: Manual loop: 
s = "hello"
result = ""

for char in s:
    result = char + result

print(result)

#The trick is char + result: each new character is added to the front of the existing result.

# Character       Result

# h               h

# e               eh

# l               leh

# l               lleh

# xo               olleh

