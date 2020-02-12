# Week 5
# Code Along 2

# number_of_scores = int(input("Enter the number of scores: "))
# scores = []
# for x in range(0, number_of_scores):
#     while True:
#         try:
#            score = int(input("What is the score #: " + str(x+1)))
#            scores.append(score)
#         except:
#             print("Invalid score value. Please try again. ")
#         else:
#             break
# try:
#     print(sum(scores)/len(scores))
# except:
#     print("Something is wrong")

# while True:
#     try:
#         email_address = input("Enter your email address: ")
#         parts = email_address.split("@")
#         name = parts[0]
#         domain = parts[1].split(".")
#         print("The email address is: ", name, domain[0], domain[1])
#         print("Thank you")
#         break
#     except:
#         none
