# Explain what "everything in Python is an object" means. Print id() and type() of an int, a string, a function, and a class.

class Student : #Class

    def square(a): #Function_square
        return a * a

    def intro(name, age):#Function_intro
        return name, age


print(type(Student)) # type() will show you the type of the class.  Ex. just like function, class, and any data_types

print(type(Student.square), type(Student.intro))# it shows type of the function

print("Sqaure is: ", Student.square(5)) #displays the square of a

print("Introduction of the student: ", Student.intro("krish", 20)) #displays introduction of the student 

#Conclusion: In python, everything is an Object just like  every single things data, numbers, string, functions and classes which are stored in the memory.
# EVery objects comes with three parts : value, type and ID(): A unique tracking serial number also addresses of the memoery..

    
