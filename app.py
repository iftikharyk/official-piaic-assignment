# Question 1 : Area of circle
# print("-------------Start Program-------------------")
# radius = float(input("Enter the radius of circle: "))
# sqradius = radius * radius
# pie = 3.142
# area = pie * sqradius
# print("Area of circle with radius " + str(radius) + " is " + str(area))
# print("--------------End Program--------------------")

# Question 2 : Check Number either positive, negative or zero
# print("-------------Start Program-------------------")
# inputted = float(input("Enter number positive or negative: "))
# if inputted >= 0:
#     print("You have entered: " + str(inputted))
#     print("The number is positive")

# elif inputted < 0:
#     print("You have entered: " + str(inputted))
#     print("The number is negative")
# else:
#     print("Invaild number")
# print("--------------End Program--------------------")

# Question 3 : Divisibility Check of two numbers
# print("-------------Start Program-------------------")
# n = int(input("Enter numerator: "))
# d = int(input("Enter denominator: "))

# def multiple(n, d):
#     return True if n % d == 0 else False

# if multiple(n, d) == True:
#     print("numerator: " + str(n))
#     print("denominator: " + str(d))
#     print("Number" + str(n) + " is Completely divisible by " + str(d))
# else:
#     print("numerator: " + str(n))
#     print("denominator: " + str(d))
#     print("Number" + str(n) + " is not Completely divisible by " + str(d))
# print("--------------End Program--------------------")

# Question 4 : Days Calculator
# print("-------------Start Program-------------------")
# from datetime import date 
  
# def numOfDays(date1, date2): 
#     return (date2-date1).days 

# date1 = date(2018, 12, 13) 
# date2 = date(2019, 2, 25) 
# print(numOfDays(date1, date2), "days")
# print("--------------End Program--------------------")

# Question 4 : Calculate Volume of a sphere
# print("-------------Start Program-------------------")
# rad = float(input("Enter radius of Sphere: "))
# cube = rad * rad * rad
# pie = 3.142
# v = pie * cube
# sphere = v * 4/3
# print("Volume of sphere with radius of " + str(rad) + " is " + str(sphere))
# print("--------------End Program--------------------")

# Question 5 : Copy string n times
# print("-------------Start Program-------------------")
# text = input("Enter some string to print: ")
# times = input("How many times you like it to print: ")
# for 
# print("--------------End Program--------------------")

# Question 5 : Check if number is Even or Odd
# print("-------------Start Program-------------------")
# num = int(input("Enter number: "))
# if num % 2 == 0:
#     print(str(num) + " is an Even Number")
# else:
#     print(str(num) + " is an Odd Number")
# print("--------------End Program--------------------")

# Question 6 : Vowel Tester
print("-------------Start Program-------------------")
word = input("Enter a letter: ")
if word == "a" or word == "A" or word == "e" or word == "E" or word == "i" or word == "I" or word == "o" or word == "O" or word == "u" or word == "U":
    print(word + " is a vovel")
else:
    print(word + " is not a vovel")
print("--------------End Program--------------------")