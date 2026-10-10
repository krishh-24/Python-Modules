#

name = "krish"
age = 20
salary = 50000.75

print("Name: %s, Age: %d, Salary: ₹%.2f" % (name, age, salary))

#.format()

name = "krish"
age = 20
salary = 50000.75

print("Name: {}, Age: {}, Salary: ₹{:.2f}".format(name, age, salary)) # 2f means 2 decimal places after .

#f string
salary = 50000.75

name = "Krish"
age = 20

print(f"My name is {name} and I am {age} years old also my salary is {salary}")

# conclusion: In Python, f-strings are preferred because they are easy to read, simple to write, and usually faster than older string formatting methods.

# An f-string is a string that starts with the letter f and lets you put variables or expressions inside {}
