#Explain the difference between int, float, complex, bool, str, NoneType. Give one practical example where using the wrong type would break your backend code (e.g. dividing by a string).

#int → whole number

#float → decimal number

#complex → real + imaginary number

#bool → True or False

#str → text

#NoneType → no value

price = "1000"  # String 
quantity = 2    # Integer

total = price / quantity

print(total)

#Python cannot divide a string by an integer. The backend expects a numeric price, but it receives text. to fix this convert string into integer.
