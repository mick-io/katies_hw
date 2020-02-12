#Week 2 in-class exercise (1)

pennies = int(input("How many pennies do you have? "))
nickels = int(input("How many nickels do you have?"))
dimes = int(input("How many dimes do you have?"))
quarters = int(input("How many quarters do you have?"))

results = pennies * .01 + nickels *.05 + dimes * .1 + quarters *.25
amount = format(results, ".2f")
print ("You have $" + str(amount) + " in change")

#Code along week 2 lab 2
# Part 1
print(True)
print(type(True))
print(1 == 1)
print(1 == 2)
print(1 != 1)
print(1 < 2)
print(1 > 2 and 2 < 5)
print(1 > 2 or 2 < 5)
print(not 1 > 2 and 2 < 5)

# Part 2
#One way condition
x = 5
if x > 0:
    print("x is positive")

print("complete")

#Two way condition
x = -1
if x > 0:
    print("x is positive")
else:
    print("x is less than 0")

#Multi-way condition
x = 10
if x > 0:
    print("x is positive")
elif x == 0:
    print ("x is zero")
else:
    print("x is less than zero")

x = 7
if x > 0:
    print("x is positive")
    if x % 2 == 0:
        print("x is even")
    else:
        print("x is odd")
else:
    print("x is not positive")
