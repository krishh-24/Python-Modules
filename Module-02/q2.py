# Prove immutability using id(): show that s = s + " world" creates a new object in memory (different id() before and after).

msg = "hello"
print(id(msg))
print(msg)

msg = msg + " world" #concatenation 
print(msg)
print(id(msg))

# Conclusion: Strings are immutable in Python. The original string "Hello" is not modified; a new string "Hello world" is created instead.

# Comparing id(s) before and after shows different IDs, it shows that msg now refers to a different object.


