#Homework 1 + 2 Review

#3.1 --> Vocab Review
#1. Git vs. Github --> Git is a local software tool used to track changes in code, whereas Github is a cloud-based service that hosts
#those Git repositories, allowing for collaboration and sharing of code with others.
#2. Terminal vs. Command line --> Terminal is a tool used to type commands on a computer, whereas a command line is a text-based method
#of interacting with the computer. 
#3. Local vs. Remote Repository --> A local repository is your personal workspace on your computer where you can write/commit code, 
#where a remote repository is the storage location where the code lives online.
#4. Version control --> A system that records changes to code files over time, allowing developers to track history, restore previous 
#versions, and collaborate simulataneously
#5. Staging area --> it is a temporary storage area that holds changes made to files in your working directory before they are formally
#committed to a local repository
#6. Git add --> a command used to move changes from your working directory to the staging area
#7. Git commit --> a command used to save changes from the staging area to the local repository
#8. Git push --> a command used to upload local repository changes to a remote repository on platforms like Github
#9. Git status --> a command used to check the current state of the working directory and staging area
#10. Git pull --> a command used to fetch and merge changes from a remote repository to your local repository
#11. pwd --> a command used to print the current working directory
#12. ls --> a command used to list the contents of a directory
#13. cd --> a command used to change the current working directory
#14. nano --> a command used to open a simple text editor in the terminal
#15. touch --> a command used to create an empty file or update the timestamp of an existing file
#16. mv --> a command used to move or rename files and directories
#17. rm --> a command used to remove files or directories
#18. cat --> a command used to display the contents of a file in the terminal

#3.2 --> A directory tree
#1. Use the command "pwd" to see what your current working directory is
#2. Use ls to see all the files in your current directory
#3. Use cp ../brianna_repo/homework.py
#4. mv ../brianna_repo/homework.py
#5. use cd ../judy_decal 
#6. use git add . and then git commit -m "added homework.py" 
#7. This error means that the local repository is out of sync with the 
#remote github repository, and you need to pull the latest changes from the remote repository before 
#you can push your local changes. This can be done by using the command "git pull origin main"
#8. Use cd ~/

#4 --> Homework 3 Review

#4.1 --> Data Types
def get_type_of_data(data):
    return type(data)


#4.2 --> Conditionals
def check_even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"


#5 --> Loops
def sum_of_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
numbers = [1, 2, 3, 4, 5]

#6 --> Homework 4 Review
#6.1 --> lists
def duplicate_list(list):
    return [item for item in list for _ in range(2)]
duplicate_list(["a", "b", "c"]) 


#6.2 --> debugging

#def square(num)
    #return num * num
#the issue was there was no colon after the function definition

def square (num):
    return num * num

#favorite problem from this set:
def sum_of_numbers(numbers):
    total = 0
    for number in numbers:
        total += number
    return total
numbers = [1, 2, 3, 4, 5]
print(sum_of_numbers(numbers)) #test

