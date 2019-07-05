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

# Question 5 : Calculate Volume of a sphere
# print("-------------Start Program-------------------")
# rad = float(input("Enter radius of Sphere: "))
# cube = rad * rad * rad
# pie = 3.142
# v = pie * cube
# sphere = v * 4/3
# print("Volume of sphere with radius of " + str(rad) + " is " + str(sphere))
# print("--------------End Program--------------------")

# Question 6 : Copy string n times
# print("-------------Start Program-------------------")
# text = input("Enter some string to print: ")
# times = input("How many times you like it to print: ")
# for 
# print("--------------End Program--------------------")

# Question 7 : Check if number is Even or Odd
# print("-------------Start Program-------------------")
# num = int(input("Enter number: "))
# if num % 2 == 0:
#     print(str(num) + " is an Even Number")
# else:
#     print(str(num) + " is an Odd Number")
# print("--------------End Program--------------------")

# Question 8 : Vowel Tester
# print("-------------Start Program-------------------")
# word = input("Enter a letter: ")
# if word == "a" or word == "A" or word == "e" or word == "E" or word == "i" or word == "I" or word == "o" or word == "O" or word == "u" or word == "U":
#     print(word + " is a vovel")
# else:
#     print(word + " is not a vovel")
# print("--------------End Program--------------------")

# Question 9 : Triangle area
# print("-------------Start Program-------------------")
# b = int(input("Input the base : "))
# h = int(input("Input the height : "))

# area = b*h/2

# print("area = ", area)
# print("--------------End Program--------------------")

# Question 10 : Calculate Interest
# print("-------------Start Program-------------------")
# amount = int(input("Enter amount: "))
# interest = float(input("Enter interest rate: "))
# years = int(input("Enter year(s): "))

# value  = amount*((1+(0.01*interest)) ** years)
# print("After " + str(years) + " years your principal amount " + str(amount) + " over an interest rate of " + str(interest) + "% will be " + str(round(value)))

# print("--------------End Program--------------------")

# Question 11 : Euclidean distance
# print("-------------Start Program-------------------")
# import math
# x1 = float(input("Enter value x1"))
# x2 = float(input("Enter value x2"))
# y1 = float(input("Enter value y1"))
# y2 = float(input("Enter value y2"))

# point1 = [x1, x2]
# point2 = [y1, y2]
# print(point1)
# print(point2)

# distance = math.sqrt( ((point1[0]-point2[0])**2)+((point1[1]-point2[1])**2) )

# print("distance = ", distance)
# print("--------------End Program--------------------")

# Question 12 : Feet to Centimeter Converter
# print("-------------Start Program-------------------")
# h_ft = int(input("Feet: "))
# h_inch = h_ft * 12
# h_cm = round(h_inch * 2.54, 1)

# print("Your height is : %d cm." % h_cm)
# print("--------------End Program--------------------")

# Question 13 : BMI Calculator
# print("-------------Start Program-------------------")
# height = float(input("Input your height in meters: "))
# weight = float(input("Input your weight in kilogram: "))
# print("Your body mass index is: ", round(weight / (height * height), 2))
# print("--------------End Program--------------------")