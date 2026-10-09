#Explain (comment) the difference between =, ==, and is. 
# Then write code proving that two variables holding the same integer 100 are is-equal, but two lists with the same contents are not is-equal. Use id() to prove it.
a = 100
b = 100

print(a is b)
print(a == b)

list1 = [11, 12, 13, 15]
list2 = [11, 12, 13, 15]

print(list1 == list2) #in this it only checks every and each elemensts of the list.
print(list1 is list2) # in this it will check memory location of the both list even if both has same elements.


#Con: ( = ) : is used for assigning some values to the variable 
# ( == ): checks for value equality in two variables, 
# while ( is ) checks for object identity.
