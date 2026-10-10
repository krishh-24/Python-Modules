#Demonstrate at least 10 string methods: .strip(), .split(), .join(), .replace(), .find(), .index(), .format(), f-strings, .upper()/.lower(), .startswith()/.endswith(), .isdigit(), .zfill().

name = input("Enter your name: ")

print("Uppercase:", name.upper()) #Uppercase
print("Lowercase:", name.lower()) #Lowercase
print("Title:", name.title()) #Gives title
print("Capitalize:", name.capitalize()) #first letter will be capital

print("Length:", len(name)) #length of the string

print("Number of 'w':", name.lower().count("w")) # count will count how many char of w in string
print("Starts with A:", name.lower().startswith("a")) #startwith checks string is startwith a or not
print("Ends with w:", name.lower().endswith("w")) #endwith checks string is endwith w or not
print("Without spaces:", name.strip()) #remove spaces 
print("Replace spaces:", name.replace("w", "p")) #replace char in string or space also 
print("Position of 'a':", name.lower().find("a")) #shows postion of the char in string

print("Only alphabets:", name.isalpha()) #checks if it is alphbet or not
print("Only numbers:", name.isdigit()) #checks if it is digits or not
print("Alphanumeric:", name.isalnum()) #checks if it is alpha-numeirc or not
print("Is lowercase:", name.islower()) #checks if it is loweercase or not
print("Is uppercase:", name.isupper()) #checks if it is upperase or not

print("O in wow or not: ", "o" in name)  # in word checks is that word in string or not
print("Words:", name.split()) #split words into list

#slicing methods: 

print("First character:", name[0]) #it shows which char is occupied on which index number in string
print("Last character:", name[-1]) #last char will print
print("character:", name[1:5]) #only 1 to 4 char will print
print("First four character:", name[:3])# before 3 only that char will print
print("First four character:", name[3:]) #after 3 every char will print
print("First four character:", name[::-1]) #for reversing whole string


name = "Krish"
age = 20

print("format(): ", "Name: {} Age: {}".format(name, age)) #used to give  format

print(f"f-string: Name: {name}, Age: {age}") #fstring mostly used thing 

print("join():", " ".join(["hello", "krish"])) #Joining two differ word into one with the use of join() and list