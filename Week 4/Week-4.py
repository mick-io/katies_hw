# # Homework week 3
# # EX 1
#
# grades = [90, 100, 70, 45, 76, 84, 93, 21, 36, 99, 100]
#
# #create counter variables
# a = 0
# b = 0
# c = 0
# d = 0
# f = 0
#
# for grade in grades:
#     if grade >= 90:
#         a += 1
#     elif 80 < grade <90:
#         b += 1
#     elif 70 < grade <= 80:
#         c += 1
#     elif 65 < grade <= 70:
#         d += 1
#     else:
#         f += 1
# print(a)
# print(b)
# print(c)
# print(d)
# print(f)

# # EX 2
#
# grades = [93, 74, 66, 98, 34, 75, 79, 83, 84, 91, 12, 69, 72]
#
# for grade in range(0, len(grades)):
#     if grades[grade] >= 90:
#         continue
#     elif 80 <= grades[grade] < 90:
#         grades[grade] += 2
#     elif 70 <= grades[grade] <= 80:
#         grades[grade] += 5
#     else: grades[grade] += 8
# print(grades)

## EX 3
## Sales = [0] * 7
#
# for s in range(0, len(Sales)):
#     query = "Enter sales for day # " + str(s + 1) + ":"
#     sale = int(input(query))
#     Sales[s] = sale
# print("Sales for the week: ", Sales)

# # EX 4
# my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
#
# x = my_list[:3]
# print(x)
#
# y = []
# for char in my_list:
#     if char == "b" or char == "c" or char == "d":
#         y.append(char)
# print(y)
#
# z = my_list[3:]
# print(z)


# # EX 5
# inventory = ["apple", "pear", "peach", "banana"]
# product = input("Enter the name of a product: ").lower()

# if product in inventory:
#     print(f"{product} is in the inventory")
# else:
#     print("item not found")


# # EX 6

# a = [1,2,3,4,5]
# b = [2,3,10,11,12,1]
# common = []
# # find all elements that exist in both lists
# for n in a:
#     if n in b:
#     # Store results in a list
#         common.append(n)
# print(common)

# # EX 7
# names = []
# # Continually...
# while True:
#     # prompts user for first names
#     name = input("Enter a first name: ")
#     # if user input = "end"
#     if name == "end":
#         # stop loop
#          break
#     if name in names:
#         print("Name already stored")
#         continue
#     # Store names in list
#     names.append(name)
# # Print after "end"
# for name in names:
#     print(name)
# # TODO: Prevent user from entering duplicate names

# # EX 8
# inventory = ["apple", "pear", "peach", "banana"]
# # Continually ask user for a product name
# while True:
#     product = input("Enter product name: ").lower()
#     if product == "end":
#         break
#     # Check for product name in inventory
#     if product in inventory:
#         # If yes, remove product from inventory
#         inventory.remove(product)
#         # print inventory
#         print(inventory) 
#     else:
#         print("Product not available")
#   # End with "end" or once list is exhausted
#     if not inventory:
#         break

# # EX 9

# products = ['peanut butter', 'jelly', 'bread']
# prices = [3.99, 2.99, 1.99]

# # Continually...
# while True:
#     # ask user for a product name
#     product = input("Enter the product for lookup: ").lower()
#     i = products.index(product)
#     # print the price of the product
#     price = format(prices[i], ".2f")
#     print("$" + price)


# # EX 10

# # ask the teach for number of students

# n_students = int(input("How many students are in the class?: "))

# # ask the teacher how many assignments

# n_assignments = int(input("How many assignments?: "))

# for n in range(n_students):
#     scores = []
#     student_number = str(n + 1)
#     print("Student #" + student_number)
#     # prompt the user to enter scores for each student
#     for assignment in range(n_assignments):
#         score = float(input("Enter scores for student: "))
#         scores.append(score)
#     # compute the average grade for each student in the class
#     grade = sum(scores) / len(scores)
#     print("Student #" + student_number, "earned a", grade, "\n")
