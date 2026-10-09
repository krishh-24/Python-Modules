#Write code showing integer caching — Python caches small ints (-5 to 256). Compare id(a) and id(b) for a = 100; b = 100 vs a = 1000; b = 1000. Explain the output.

#Inter caching: Python typically caches small integers from -5 to 256. This means that multiple references to the same small integer may point to the same object in memory. 

#Small interger caching:
a = int("100")
b = int("100")

print("Id of A: ",id(a))
print("Id of b: ",id(b))

print(a is b)

#Larger Integers:

a = int("1000") #coverts str into int
b = int("1000")

print("Id of A: ",id(a))
print("Id of b: ",id(b))

print(a is b)


#conclusion: Python keeps some small integers, usually from -5 to 256, ready to reuse. Python can reuse the same integer object.Python reuses the small integer object, so id(a) and id(b) are the same, and a is b returns True.

#Since 1000 is outside of the small-integer cache, Python typically creates two separate integer objects. Therefore, their IDs differ, and a is b is usually False.