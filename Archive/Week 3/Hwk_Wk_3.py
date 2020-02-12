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

# EX 5
products = ["apple", "pear", "peach", "banana"]
options = input
