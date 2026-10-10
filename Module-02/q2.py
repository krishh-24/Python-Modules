# Prove immutability using id(): show that s = s + " world" creates a new object in memory (different id() before and after).

msg = "hello"
print(id(msg))
print(msg)

msg = msg + " world"
print(msg)
print(id(msg))