#Slicing mastery: given s = "backend_developer", extract: last 4 characters, every 2nd character, reversed string, first 7 characters — all using slicing only.

s1 = "hello_python" 

print(s1[-4:]) #it prints last 4 digits.
print(s1[: :2]) #skips every 2 char
print(s1[::-1]) #used for reversing string.
print(s1[:7]) #first 7 letters 
print(s1[6:]) #last 6 letters 
