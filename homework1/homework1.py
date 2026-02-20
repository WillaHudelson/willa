#File: homework1. py
# --- Variables and Data Types ---
a = 10
print (a)
print (type(a)) #a is an integer, a whole number with no decimals
b = 1.5
print (b)
print (type(b)) #b is a float, a decimal
c = 3j
print (c)
print (type(c)) #c is a complex data type, where 3 is the coefficient and j is an 
#imaginary number
d = "hello"
print (d)
print(type(d)) #d is a string, a word/text
e = [1, 2, 3]
print (e)
print(type(e)) #e is a list, an ordered sequence
f = {"name": "Ellen", "favorite fruit": "strawberry"}
print (f)
print(type(f)) #f is a dictionary, it constists of the key:value components and are
#mutable
g = (1,2)
print (g)
print(type(g)) #g is a tuple, it consists of an ordered sequence and is immutable
h = ["apple", "banana", "strawberry"]
print (h)
print(type(h)) #h is a list, an ordered sequence
i = True
print(i)
print(type(i)) #i is a boolean, a representation of truth values (true/false)
j = None
print (j)
print(type(j)) #j is a NoneType, a null result or absense of a value
k = [True, "blue", 12]
print (k)
print(type(k)) #k is a list, an ordered sequence
l = str(14)
print (l)
print(type(l)) #l is a string, a word/text
m = 1e4
print (m)
print(type(m)) #m is a float, a decimal 
#Question 1: I found 9 different data types
#Question 2: Integer, Float, Complex, String, List, Dictionary, Tuple, Boolean, 
#NoneType
#Question 3: b and m = float, d and l = string, e, h, and k = list
#Question 4: l is a string because it has the str() in it, which is also the reason
#l is not an integer, because the str() defines it as string
#Question 5:
numbers = {2, 4, 6, 6, 2, 8}
print(numbers)
print(type(numbers)) #numbers is a set, an sequence of unordered values

#---Booleans---
print (10>9) #True, 10 is indeed greater than 9
print (10==9) #False, 10 is not equal to 9
print (10<=9) #False, 10 is not greater than or equal to 9
print(bool(123)) #True because it's not equal to 0
print(bool(["apple", "cherry", "banana"])) #True because it's not empty
print(bool(True)) #True because it states true
print(bool(False)) #False because it states false
print(bool(0)) #False because it's equal to 0
print(bool("")) #False because it's empty
print(bool(" ")) #True because it's not empty (a space is something)
print(bool(())) #False because it's empty
print(bool([])) #False because it's empty
print(bool({})) #False because it's empty
print(bool(True and False)) #False because something can't be true AND false at the same time
print(bool(True and True)) #True because both are true
print(bool(False and False)) #False because both are false
print(bool(True or False)) #True because it has the potential to be true
print(bool(False or False)) #False because it has the potential to be false
print(bool(not(False))) #True because it's not false
print(bool(not(True))) #False because it's not true
#Question 1: If something is explicitly stated as true or false, it will display as true or false respectively. Also if 
#something is empty or 0, then it will be false, otherwise, it will be true. 
#Question 2: The bool(" "), because I thought a space would mean its empty, however that was not the case
#Question 3: print(bool("hehehaha")), it's true because it's not empty
#Question 4: print(bool(5>7)), it's false because 5 is not greater than 7

#---Operators---
#-Arithmetic Operators-
print(10+5) #15, the (+) performs addition
print(10-5) #5, the (-) performs subtraction
print(2*4) #8, the (*) performs multiplication 
print(6/3) #2, the (/) performs division
print(5%2) #1, the (%) displays the remainder
print(3**2) #9, the (**) is equivilent to (^), meaning it's to the power
print(15//2) #7, the (//) performs integer division and rounds down
#-Comparison Operators-
print(5==2) #False because 5 does not equal 2 (and the (==) represents an equal sign)
print(10 != 10) #False because the (!=) represents 'not equal to', and 10 IS equal to 10
print(2<5) #True because 2 is less than 5
print(12>5) #True because 12 is greater than 5
print(5<=6) #True because 6 is greater than or equal to 5 (and the <= is greater than or equal to)
print(1>=10) #False because 1 is not greater than or equal to 10
#-Assignment Operators-
x=5
x += 5
print(x) #10, the (+=) adds the value on the right to the variable on the left 
x -= 4 
print(x) #6, the (-=) subtracts the value on the right from the variable on the left
x *= 3
print(x) #18, the (*=) multiplies the variable on the left by the value on the right
#-Logical Operators-
#Question 1: the operator "and" is used to check if both statements are true --> print(bool(5>3 and 2<4)), this is true 
#because both statements are true --> print(bool(5>3 and 2>4)), this is false because one statement is false
#Question 2: the operator "or" is used to check if at least one statement is true --> print(bool(5>3 or 2>4)), this is 
#true because at least one statement is true --> print(bool(5<3 or 2>4)), this is false because both statements are false
#Question 3: the operator "not" is used to check if a statement is false --> print(bool(not(3>5))), this is true because 3
#is not greater than 5 --> print(bool(not(5>3))), this is false because 5 is greater than 3
#-More Questions-
#Question 1: the difference between (/) and (//) is that (/) performs regular division and can result in a decimal,
#while (//) performs integer division and rounds down to the nearest whole number
#Question 2: the difference between (%) and (//) is that (%) gives the remainder of a division operation,
#while (//) gives the quotient of a division operation rounded down to the nearest whole number
#Question 3: the operator I would use to calculate the remainder when dividing two numbers is (%) --> print(10%3), 
#this gives a result of 1 because 3 goes into 10 three times with a remainder of 1
#Question 4: Assignment operators work by assigning a value to a variable and then performing an operation on that variable
#---Strings---
my_string = "Hello"
print(my_string) #Prints: Hello
print(my_string[0]) #Prints: H because the 0th character is H
print(my_string[1]) #Prints: e because the 1st character is e
print(my_string[2]) #Prints: l because the 2nd character is l
print(my_string[3]) #Prints: l because the 3rd character is l
print(my_string[4]) #Prints: o because the 4th character is o
print(my_string[-1]) #Prints: o because the -1st character is o
print(my_string[1:3]) #Prints: el because it starts at the 1st term and goes up to but does not include the 3rd term
print(my_string[0:5:2]) #Prints: Hlo because it starts at the 0th term and goes up to but does not include the 5th term, 
#and it takes every 2nd character
print(len(my_string)) #Prints: 5 because there are 5 characters in the string
my_string = "Hello, goodbye "
print(my_string) #Prints: Hello, goodbye
print(my_string*7) #Prints: Hello, goodbye 7 times because the (*) indicates that the string should be repeated a 
#specified number of times
#-Questions-
#Question 1: the term slicing means to extract a portion of a string by specifying a range of indices
#Question 2: 
name = "Oski"
print("Hello, my name is", name) #Prints: "Hello, my name is Oski" because the print function will print what was commanded
#and the defined variable
#Question 3: 
name = "Oski"
print(f"Hello, my name is {name}") #Prints: "Hello, my name is Oski" because the f-string allows for the inclusion of 
#variables
#Question 4: The difference between the last two statements is that the first one uses a comma to separate the string 
#from the varaiable, while the second one uses an f-string to include the variable directly within the string
#---Terminal Commands---
#cd
#Changes directories, you use it to move from one folder to another
#Example: cd Desktop
# ls
# Lists the contents of a directory, such as files and folders
# Example: ls in desktop would list all the contents of the desktop
#ls-a
# Lists all contents of a directory, including hidden files and folders
#Example: ls -a desktop
#mkdir
# Creates a new directory with the specified name
#Example: mkdir new_folder
#cat
#Displays the contents of a file
#Example: cat file.txt
#pwd
#Prints the current working directory
#Example: pwd in descktop would print the file path to the desktop
#cd..
#Moves up one directory level
#Example: if you are in the desktop and you type cd.., it will move you up to the home directory
#cd.
#Stays in the current directory
#Example: if you are in the desktop and you type cd., it will keep you in the desktop
#cd~
#Moves to the home directory
#Example: if you are in the desktop and you type cd~, it will move you to the home directory
#cp
#Copies a file or directory from one location to another
#Example: cp file.txt new_folder/ would copy the file.txt into the new_folder
#mv
#Moves a file or directory from one location to another
#Example: mv file.txt new_folder/ would move the file.txt into the new_folder
#rm
#Removes a file or directory
#Example: rm file.txt would remove the file.txt
#clear
#Clears the terminal screen
#Example: clear would get rid of the terminal screen
#grep
#Searches for a specific pattern in a file and displays the matching lines
#Example: grep "hello" file.txt would search for the word "hello" in file.txt and display the lines that contain it
#-Questions-
#Question 1: 
#command 1 - python3 homework1.py, this command runs the python file named homework1.py
#command 2 - touch new_file.txt, this command creates a new file named new_file.txt
#command 3 - bin/bash, this command opens the bash terminal
#Question 2: The difference between ls and ls -a is that ls lists the contents of a directory, while ls -a lists all 
#contents of a directory, including hidden files and folders
#Question 3: A hidden file is a file that is not visible in the directory by default
#Question 4: 
#Flag 1 - -r, this flag is used with the rm command to remove directories and their contents recursively
#Flag 2 - -i, this flag is used with the rm command to prompt the user for confirmation before deleting each file
#Flag 3 - -v, this flag is used with the rm command to display the name of each file as it is being removed
#---Running Your Script---
#-In Your VS Code Terminal-
