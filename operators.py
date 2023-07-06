# operators
#Addition: +
#Subtraction:-
#Multiplication:*
#Division:/
#Exponent: **(multiply a number twice)
#Floor division: //
#remainder: %

x = 5
result = x+10 #addition
print(result)

z = 20
result = z * 4 # multiplication

print(result)

y = 50
result = y**2  #exponent
print(result)

r = 30
result = r/30 # division
print(result)

# concantenating strings
string1 = "Dorothy"
string2 = "Akoth"

print(string1 + " " + string2)

"QUIZ 1"
" suppose you are a university student and you need to pay &4535 tuition fee for the "
"next semester. The college is giving you a discount of 10% on early payment tuition fee"
" you decided to make an early payment. Can you find out how much money"
"you have to pay?"

fee = 4535
discount_percent = 10
discount_amount = (discount_percent/100) * fee
discount_fee = fee - discount_amount
print(discount_fee)

"QUIZ 2"
" create a program to convert distance in kilometers to miles"
"formular: kilometer -> 0.621371"
#  Solved the above quiz by looking at the following
# Operators
# input and output in python
# datatypes

kilometers = float(input("Enter value in Km: "))
convert_km = 0.621371

miles = kilometers * convert_km
print(kilometers)
print(miles)

" Write a python program to find the square root for positive numbers "


num = 16

num_sqrt = num** 0.5
print(num_sqrt)
print(num)


# Write a python program for calculating the area of a triangle
# Python Program to find the area of triangle

a = 4
b = 5
c = 6

# calculate the semi-perimeter
s = (a + b + c) / 2
# calculate the area of the triangle
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print(area)