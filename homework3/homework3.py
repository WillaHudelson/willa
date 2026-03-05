#3 - Print Functions
def say_goodbye(yall):
    print("goodbye,", yall)
say_goodbye("yall")

def print_circle_area():
    radius = 9
    pi = 3.14159
    area = pi * radius**2
    print("The area of the circle is:", area)
print_circle_area()

#4 - Return Functions
def subtract (a,b):
    return a - b

def multiply (a,b):
    return a * b

def divide (a,b):
    return a / b

#5 - Conditionals

def what_to_wear(temp):
    if temp < 30:
        return "Wear a puffer"
    elif temp > 85:
        return "Wear a tank top"
    else: 
        return "wear a tank top"
temp = [30, 45, 60, 75, 90]
low = min(temp)
high = max(temp)

def is_weekend(day):
    if day == "6" or day == "7":
        return True
    else:
        return False


def fuel_efficiency(distance, fuel_used):
    return distance / fuel_used

def encrypt_number(num):
    last_digit = num % 10
    remaining_digits = num // 10
    multiplier = 10 ** (len(str(remaining_digits)))
    return last_digit * multiplier + remaining_digits

#6 - Loops

def power(x,y):
    result = 1
    for i in range(y):
        result *= x
        result = result * x
    return result

#return function to find a minimum FOR
def find_minimum(numbers):
    smallest = numbers[0]
    for num in numbers:
        if num < smallest:
            smallest = num
    return smallest
#return function to find a maximum FOR
def find_maximum(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest
#return function to find a minimum WHILE
def find_minimum(numbers):
    smallest = numbers[0]
    i = 1
    while i < len(numbers):
        if numbers[i] < smallest:
            smallest = numbers[i]
        i += 1
    return smallest
#return function to find a maximum WHILE
def find_maximum(numbers):
    largest = numbers[0]
    i = 1
    while i < len(numbers):
        if numbers[i] > largest:
            largest = numbers[i]
        i += 1
    return largest

def sum_of_digits(num):
    total = 0
    while num > 0:
        digit = num % 10
        total += digit
        num //= 10
    return total

#FAVORITE FUNCTION
def is_weekend(day):
    if day == "6" or day == "7":
        return True
    else:
        return False
print(is_weekend("6")) #example
print(is_weekend("3")) #exmaple