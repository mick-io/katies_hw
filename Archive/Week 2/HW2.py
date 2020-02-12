# HW2
# EX 2.1
# while True:
#     user_input = int(input("Enter the coin value: "))
#     if user_input == 1:
#         print("That's a penny!")
#     elif user_input == 5:
#         print("That's a nickel!")
#     elif user_input == 10:
#         print("That's a dime!")
#     elif user_input == 25:
#         print("That's a quarter!")
#     elif user_input == 50:
#         print("That's a half dollar!")
#     else:
#         print("I don't know this currency")

# EX 2.2
# while True:
#     user_input = input("Enter a number, from 1 to 10. Enter Q to quit ")
#     if user_input == "Q":
#         break
#     user_input = int(user_input)
#     if user_input < 0 or user_input > 10:
#         print("Invalid entry")
#     elif user_input % 2 == 0:
#         print("Your number is even")
#     else:
#         print("Your number is odd")
#     if user_input in (2, 3, 5, 7):
#         print("Your number is prime")

# EX 2.3
# while True:
#     user_input = input("Enter price of item, enter 'Q' to quit: ")
#     if user_input == "Q":
#         break
#     price = float(user_input)
#     discount = 0.0
#     if price <= 0:
#         print("invalid value")
#     elif price >= 10 and price <= 50:
#         discount = price * .10
#     elif price > 50:
#         discount = price * .20
#     price = format(price - discount, ".2f")
#     print("Your total is $", price)

# EX 2.4
# starting_number = int(input("Enter a starting number: "))
# ending_number = int(input("Enter an ending number: "))
# odd_even = input("even or odd? ")
#
# if odd_even.lower() == "even":
#     while starting_number > ending_number:
#         if starting_number % 2 == 0:
#             print(starting_number)
#         starting_number -= 1
# elif odd_even.lower() == "odd":
#     while starting_number > ending_number:
#         if starting_number % 2 != 0:
#             print (starting_number)
#         starting_number -= 1

# EX 2.5
# user_input = int(input("Enter the number of products you'd like to purchase" ))
# number_list = [None] * user_input
# for x in range(user_input):
#     number_list[x] = float(input("What is the price for item number " + str(x+1) + "?"))
# print ("Total cost: "+str(sum(number_list)))

# EX 2.6
# sales_tax = 0.07

# while True:
#     # ask user for a series of product price
#     item_price = float(input("Enter the price of the item: "))
#
#     # compute sales tax (7%)
#     item_tax = item_price * sales_tax
#
#     # print out new price to user.
#     item_total = format(item_price + item_tax, ".2f")
#     item_tax = format(item_tax, ".2f")
#     print(f"Tax on this item is ${item_tax}; total price: ${item_total}")
#
#     # ask the user if they want another price
#     user_input = input("Enter another price? (y or n): ")
#
#     # repeat or end based on user response()
#     if user_input == "n":
#         break


# # EX 2.7
#     total_due, total_tax = 0.0, 0.0
#     sales_tax = 0.07
#
#     while True:
#         # ask user for a series of product price
#         item_price = float(input("Enter the price of the item: "))
#
#         # compute sales tax (7%)
#         item_tax = item_price * sales_tax
#
#         # print out new price to user.
#         item_total = format(item_price + item_tax, ".2f")
#         item_tax = format(item_tax, ".2f")
#         print(f"Tax on this item is ${item_tax}; total price: ${item_total}")
#
#         # add to total_due & total_tax
#         total_due += float(item_total)
#         total_tax += float(item_tax)
#
#         # ask the user if they want another price
#         user_input = input("Enter another price? (y or n): ")
#
#         # repeat or end based on user response
#         if user_input == "n":
#             break
#
#     # Print totals
#     total_due, total_tax = format(total_due, ".2f"), format(total_tax, ".2f")
#     print(f"Total amount due: ${total_due}")
#     print(f"Total tax due: ${total_tax}")


# # EX 2.8
# correct_answer = 4.0
# # Continually ask math questions
# while True:
#     user_answer = float(input("What is 2 + 2? : "))
#
#     # if answered correctly...
#     if user_answer == correct_answer:
#         print("Correct!")
#         break
#     # else ...
#     print("Wrong, try again.")


# # EX 2.9
#     # generate 2 random numbers
#     import random
#     n1, n2 = random.randint(1, 100), random.randint(1, 100)
#     correct_answer = n1 + n2
#
#     # enter while loop
#     while True:
#         # prompt user what n1 + n2?
#         user_input = float(input(f"What is {n1} + {n2}? : "))
#
#         # break if correct
#         if user_input == correct_answer:
#             print("Correct!")
#             break
#         # else ...
#         print("Incorrect, try again.")
