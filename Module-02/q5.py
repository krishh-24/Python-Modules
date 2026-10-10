# Explain the difference between .find() and .index() when the substring is not found — show the actual error/output.

# In Python, both .find() and .index() are used to search for a substring inside a string. The main difference is it happens when the substring is not found.

# If the substring is not found, .find() returns -1. It does not gives you an error
# If the substring is not found, .index() raises a ValueError..

message = "hello python"

print(message.find("python")) # it will shows you 6 num coz python starts at 6 index in string.
print(message.find("world")) # it will shows you -1 because hello python does not have world in string

# index(): 

print(message.index("python")) #it will shows you 6 num coz python starts at 6 index in string.
print(message.index("world")) #it will gives you value error that substring not found
