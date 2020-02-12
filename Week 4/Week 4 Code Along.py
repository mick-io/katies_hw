# #Code-Along Lab 1
#
# prices = [1.10, 0.99, 5.75]
# for item in prices:
#     print("Original price: ", item)
#     item *= 1.07
#
# print(prices)
#
# i = 0
# for item in prices:
#     print("Original price: ", item)
#     prices[i] *= 1.07
#     prices[i] = format(prices[i], ".2f")
#     i += 1
#
# print(prices)
#
# position = 0
# while position < len(prices):
#     prices[position] *= 1.07
#     position += 1
#
# print(prices)

# my_numbers = "10, 20, 30, 40, 50, 60"
# print(type(my_numbers))
#
# number_list = my_numbers.split(",")
# print(number_list)
#
# number_list[1] = number_list[0]
# print(number_list)

# tim = "16:30:10"
# hrs, mins, secs = tim.split(":")
# print(hrs, mins, secs)




# Code Along Lab 2

# Dictionaries
# my_dict = {
#     #create a key (EX: NAME), separate with a colon and specify the value (EX: THOR)
#     "name": "Thor",
#     "age": "25"
#
# }
# print(my_dict)

# example_dict = {
#     "animals": ["dog", "cat", "fish"],
#     "number": 1,
#     "name": "Odin",
#     "a_boolean": True,
#     "another_dict": {
#         "You could": "Kepp going",
#         "Like this": "forever"
#     }
# }
#
# for key in example_dict:
#     print(key)
#
# for item in example_dict.items():
#     print(item)
#
# for value in example_dict.values():
#     print(value)
#
# a_dictionary = {"color": "blue", "fruit": "apple", "pet": "dog"}
# for key in a_dictionary:
#     print(key, "->", a_dictionary[key])

# seasons = {
#     "Fall": ["September", "October", "November"],
#     "Spring": ["March", "April", "May"],
#     "Summer": ["June", "July", "August"]
# }
#
# winter_seasons = {"Winter": ["December", "January", "February"]}
# print(seasons)
#
# for k, v in seasons.items():
#     print(k + " : ", v)

# # Sets
# small_primes = set()
# small_primes.add(2)
# small_primes.add(3)
# small_primes.add(5)
#
# small_primes.add(1)
# small_primes.remove(1)
#
# print(small_primes)
# print(3 in small_primes)
# print(4 in small_primes)
# print(4 not in small_primes)
# small_primes.add(3)
# print(small_primes)


# # Tuples
# t = ()
# t = "a", "b", "c", "d"
# print(t)
#
# print(type(t))

# Code Along Lab 3

# def hello_world():
#     x = 10
#     x += 1
#     print("Hello World")
#
# hello_world()

# def format_name(first_name, last_name):
#     return first_name + " " + last_name
#
# name = format_name("John", "DeGrey")
# print(name)

# x = [1,2,3]
#
# def func(y):
#     y[1] = 42
#
# func(x)
# print(x)

