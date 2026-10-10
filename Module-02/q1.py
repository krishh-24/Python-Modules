#Create a string s = "hello". Try to change s[0] = "H" — capture and print the error. Explain why strings are immutable in Python.

# In Python, strings are immutable, meaning their characters cannot be changed after the string is created.

s = "krish"
s[0] = "i"

print(s) #it wiill show you type-error

# Cannot modify individual characters: s[0] = "i" raises a TypeError because string characters cannot be reassigned.

# Memory efficiency: Immutability allows Python to optimize string storage and reuse. 
# if you still wannna change the string charactrer create a new string to print modified value instead of changning exisiting string.

s = "krish"
s = "i" + s[1:]


print(s)
