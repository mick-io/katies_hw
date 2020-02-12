# Week 5
# Homework

# 1
# try:
#     file_io = open("./most_popular_words_in_english.txt", "r")
#     most_popular_words = file_io.read().split("\n")
#     word = input("Type an English word: ")
#     if word in most_popular_words:
#         print("This is one of the most popular words in English!")
#
#     else:
#         print("This is not one of the top 100 words in English")
# except:
#     print("Something went wrong!")
#

# 2
# try:
#     username = input("Enter your username: ")
#     password = input("Enter your password: ")
#     write_text = username + "\n" + password
#     file_io = open("./security.txt", "w+")
#     file_io.write(write_text)
# except:
#     print("Something went wrong.")

# 3
# try:
#     # retrieve stored values
#     file_io = open("./security.txt", "r")
#     credentials  = file_io.read().split("\n")
#     stored_username, stored_password = credentials[0], credentials[1]
#     # Obtain user input
#     input_username = input("Enter your username: ")
#     input_password = input("Enter your password: ")
#     # compare stored values to user input
#     if input_username != stored_username or input_password != stored_password:
#         print("Invalid credentials.")
#     else:
#         print("Authentication successful.")
# except:
#     print("Something went wrong!")


