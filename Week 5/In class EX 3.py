# Week 5
# In-class Exercise 3

# # 1
#
# while True:
#     valid_number = input("Enter a number: ")
#     try:
#         valid_number = int(valid_number)
#         print("You've entered a valid number!")
#         break
#     except ValueError:
#         print("You did not enter a valid number")
#

# # 2
# filename = "pi_digits.txt"
#
# with open(filename, 'a') as file_object:
#     file_object.write("I don't understand snake math.\n")
#     file_object.write("But I love snake jazz.\n")


# 3
#Write a program that prompts the user for a file name.
#If the file exists, open it and print each line.
#If the file does not exist, handle the open file exception and print a message stating that the file was not found.
#
#
# file_name = input("Enter a file name")
#
# filename = "pi_digits.txt"
#
# with open(filename) as file_object:
#     try:
#         for line in file_object:
#         print(line.rstrip())
#
#     except ValueError:
#         print("No such file exists")


