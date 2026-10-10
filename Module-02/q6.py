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

