# # EX 1

# def first():
#     print("####")

# def second():
#     print("#  #")

# def third():
#     print (" ## ")

# def fourth():
#     print (" #  ")

# def fifth():
#     print (" ## ")

# def sixth():
#     print("#  #")

# def seventh():
#     print("####")
#
# first()
# second()
# third()
# fourth()
# fifth()
# sixth()
# seventh()

#################################################################################################

# # EX 2
# # Write function that converts a number from feet to inches
# n_inches_per_foot = 12
# n_feet_per_meter = 3.281
#
# def feet_to_inches(n_feet):
#     return n_feet * n_inches_per_foot
#
# def feet_to_meters(n_feet):
#     return n_feet / n_feet_per_meter
#
# for n_feet in range(10):
#     n_inches = feet_to_inches(n_feet)
#     n_meters = feet_to_meters(n_feet)
#     print(n_feet, "feet")
#     print(n_inches, "inches")
#     print(n_meters, "meters")

#################################################################################################

# # EX 3
# # Write a function that rolls two dice.
# import random
#
# def roll_die(sides):
#     # Create dice
# 	d1 = random.randint(1, 6)
# 	d2 = random.randint(1, 6)
#
# 	# return ASC
# 	if d1 < d2:
# 		return d1, d2
# 	else:
# 		return d2, d1
#
# # Roll
# for n in range (6, 11):
# 	die1, die2 = roll_die(n)
# 	print(n, "sided die roll:", die1, "and", die2)

#####################################################################################################

# # EX 4
# techinical_terms = dict()
# techinical_terms["dict"] = "stores key/value pair"
# techinical_terms["list"] = "stores a value at each index"
# techinical_terms["map"] = "see dict"
# techinical_terms["set"] = "stores unordered unique elements"
# techinical_terms["exit"] = ""
#
# while True:
#     # Getting 'key' from user
#     user_input = input("Enter a term for lookup: ")
#
#     # Checking break condition
#     if user_input == "exit":
#         break
#
#     # Checking for memebership
#     if user_input in techinical_terms:
#
#         # Obtaining 'value'
#         definition = techinical_terms[user_input]
#
#         # Printing results
#         print(f"{user_input}: {definition}\n")
#     else:
#         print("Term not found")
