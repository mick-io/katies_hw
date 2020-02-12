## Week 3 In-Class Exercises
## 1.1
# Colors = ["cyan", "yellow", "magenta", "black", "white"]
# print(Colors)
# print(len(Colors))
# print(Colors[4])
# print(Colors[:])
# print(Colors[3:])
# print(Colors *2)

## 1.2
# Colors = ["cyan", "yellow", "magenta", "black", "white", "purple"]
# print(Colors)
# Colors[5] = "pink"
# print(Colors)

# # 2.1 Shapes
# shapes = ["square", "circle"]
# #print(shapes)
# shapes.append("triangle")
# print(shapes)
# shapes.insert(4, "rectangle")
# print(shapes)
# shapes.remove("rectangle")
# print(shapes)
# del shapes[2]
# print(shapes)
#
# # 2.2 Sorting
# # Using the sort function, sort this list in numerical order and print it:
# ages = [27, 60, 14, 35, 3, 76]
# ages.sort()
# print(ages)
#
# names = ["Quinn", "John", "Amber", "Kim"]
# names.sort()
# print(names)
#
# stats = [[3, 2], [1, 2], [1, 1], [3, 1]]
# stats.sort()
# print(stats)
#
# #2.3 Min-Max
# numbers = [6, 10, 3, 24, 79, 24]
# print(min(numbers))
# print(max(numbers))

# For Loops
# 1 Input with a for-loop
# n_numbers = int(input("How many numbers do you want to add?: "))
# total = 0.0
# for n in range (n_numbers):
#     input_n = float(input("Provide a number: "))
#     total += input_n
# print(total)

# # 2 Find the vowels
# vowels = ["a", "e", "i", "o", "u"]
# phrase = input("Enter a word or phrase: ")
# n_vowels = 0
# for char in list(phrase):
#     if char in vowels:
#         n_vowels += 1
# print(n_vowels)

names1 = ['Jane', 'Barry', 'Kipp', 'Matt']

names2 = names1

names3 = names1[:]

names2[0] = 'Alice'

names3[1] = 'Bob'

sum = 0

for ls in (names1, names2, names3):

    if ls[0] == 'Alice':

        sum += 1

    if ls[1] == 'Bob':

        sum += 10

print(sum)