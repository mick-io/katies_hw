# # def func(num1, num2):
# #     if num1 < 0:
# #         return
# #     else:
# #         return num1 + num2
# # x = func(2, 4)
# # print(x)
#
# def print_dict(dictionary):
#     keys = list(dictionary.keys())
#     values = list(dictionary.values())
#
#     for i in range(0, len(keys())):
#         k = keys[i]
#         v = values[i]
#         print(format(str(k), str(v)))
#
# example_dict = {
#     "name": "Thor",
#     "age": 25
# }
#
# print_dict(example_dict)

# def sum_two_numbers(a,b):
#     return a + b
#
# c = int(input("Enter a number: "))
# d = int(input("Enter another number: "))
#
# e = sum_two_numbers(c,d)
# print(e)

# def multiply_by(a, b=2)
#     return a * b
#
# print (multiply_by(12))

# def mod_div(a, b):
#     return a // b, a % b
#
# print(mod_div(20,7))
# print ("a", "b", "c")
# multiply_by(2,3,4)

# def func1(*args):
#     print(args)
#
# func1(1, 23, 43, 345, 3523, 4534, 4536, 56, 56)

# def db_connect(**options):
#     conn_string = {
#         "host": options.get("host", "127.0.0.1"),
#         "port": options.get("port", 8001),
#         "user": options.get("user", "admin"),
#         "pwd": options.get("pwd", "")
#     }
#     print(conn_string)
#
# db_connect(host = "192.1.1.10", port=12202, user ="Thor")

def func3(*a, c):
    print(a,c)

func3(1,2,3,4,5, c=7)
