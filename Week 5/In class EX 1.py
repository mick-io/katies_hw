# # Week 5
# # In-class Exercise 1

# def name(first, middle, last):
#     return f"{first} {middle} {last}".title()
#
# full_name = name("katie", "k", "zuppke")
# print(full_name)

# # Write a function that takes a string and returns a dictionary
# # with each word as the key and the count of that word as the value.
# def string_to_dictionary(strng):
#     strng = strng.lower()
#     new_dict = dict()
#     words = strng.split()
#
#     for letter in words:
#         if letter in new_dict:
#             new_dict[letter] += 1
#         else:
#             new_dict[letter] = 1
#
#     return new_dict
#
# my_var = "I don't understand snake math"
# print(string_to_dictionary(my_var))
