#3 - Lists

#3.1 - List Operations
favorite_foods = ["shrimp_fried_rice", "tiramisu", "pho", "caprese_salad", "zucchini_bread"]
print(favorite_foods [1])
print(favorite_foods [-1])
favorite_foods.append ("garlic_naan")
new_item = "apple"
favorite_foods.insert (0, new_item)
favorite_foods.remove ("tiramisu")
print(len(favorite_foods))
for word in favorite_foods:
    print(word.upper())
new_list = [favorite_foods[0], favorite_foods[-1]]
print(new_list)
if "potato" in favorite_foods:
    print("A potato!")
else:    print("No potato!")

#3.2 - Slicing and Striding
numbers = (list(range(0, 21)))
def get_first_15(numbers):
    return numbers [:15] 
def get_every_5 (lst):
    return lst [::5]
def reverse_and_stride (lst):
    reversed_list = lst [::-1]
    return reversed_list [::3]
step_1 = get_first_15 (numbers)
step_2 = get_every_5 (step_1)
step_3 = reverse_and_stride (step_2)
#print(step_1)
#print(step_2)
#print(step_3)

#3.3 - Nested Lists
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]
numbers = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#print(numbers[2])
#print(numbers [1][1])
numbers.append ([10, 11, 12])
def sum_nested (numbers):
    total = 0
    for row in numbers:
        for item in row:
            total += item
    return total
#print(sum_nested (numbers)) #this is a test to see if the function works

#3.4 - Create a 5x5 List
def my_5x5_list():
    list_5x5 = []
    numb = 1
    for i in range(5):
        row = []
        for j in range(5):
            row.append(numb)
            numb += 1
        list_5x5.append(row)
    return list_5x5
result_5x5 = my_5x5_list()
#print(result_5x5)
def replace_multiples_of_3(list_5x5):
    updated_list = []
    for row in list_5x5:
        updated_row = []
        for item in row:
            if item % 3 == 0:
                updated_row.append("?")
            else:
                updated_row.append(item)
        updated_list.append(updated_row)
    return updated_list
updated_5x5 = replace_multiples_of_3(result_5x5)
#print(updated_5x5)
def sum_of_rows(list_5x5):
   total = 0
   for row in list_5x5:
         for item in row:
            if item != "?":
                total += item
   return total
sum_rows = sum_of_rows(updated_5x5)
#print(sum_rows)

#4 - Dictionaries
#4.1 - Dictionary Operations
ages = {
    "Katie": 30, 
    "Mariam": 42,
    "Safia" : 25,
    "Mira": 48
}
#print(ages["Katie"])
ages.update({"Mira": 100})
ages.setdefault("Milana", 52)
del ages["Mariam"]
#for name, age in ages.items():
    #print(f"{name} is {age} years old.")

#Favorite Code to Run

favorite_foods = ["shrimp_fried_rice", "tiramisu", "pho", "caprese_salad", "zucchini_bread"]
print(favorite_foods [1])
print(favorite_foods [-1])
favorite_foods.append ("garlic_naan")
new_item = "apple"
favorite_foods.insert (0, new_item)
favorite_foods.remove ("tiramisu")
print(len(favorite_foods))
for word in favorite_foods:
    print(word.upper())
new_list = [favorite_foods[0], favorite_foods[-1]]
print(new_list)
if "potato" in favorite_foods:
    print("A potato!")
else:    print("No potato!")