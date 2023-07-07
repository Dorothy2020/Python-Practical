# Introduction to Python Function
# function is a block of code that runs the specific task

def greet(name):
    print("Hello", name)

greet("jackie")  # jack is an argument


# passing multiple arguments

def add_numbers(n1, n2):
    result = n1 + n2
    print("The sum is:", result)


number1 = 2.6
number2 = 3.4

add_numbers(number1, number2)


# return a value from a function
def add_numbers(n1, n2):
    result = n1 + n2
    return result


number1 = 2.6
number2 = 3.4

result = add_numbers(number1, number2)
print("The sum is", result)

# print the length of the list
marks = [50, 60, 30, 20]
length = len(marks)
print("Length is :", length)

marks_sum = sum(marks)
print("The total marks you got is", marks_sum)


# function to find average marks
def find_average_marks(marks):
    sum_of_marks = sum(marks)
    total_subjects = len(marks)
    average_marks = sum_of_marks / total_subjects
    return average_marks


# calculate the grade and return it
def compute_grade(average_marks):
    if average_marks >= 80:
        grade = 'A'
    elif average_marks >= 60:
        grade = 'B'
    elif average_marks >= 50:
        grade = 'C'
    else:
        grade = 'F'
        return grade


marks = [60, 30, 75, 40, 67]
average_marks = find_average_marks(marks)
print("Your average marks is :", average_marks)
grade = compute_grade(average_marks)
print("Your grade is :", grade)



"QUIZ CHALLENGE"
" Create a program to add and multiply two numbers? For this "
"create two functions , the function call. and the results should be printed from outside the function"


def add_numbers(a, b):
    return a + b


def multiply_numbers(a, b):
    return a * b


number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

sum_result = add_numbers(number1, number2)
product_result = multiply_numbers(number1, number2)

print("Sum:", sum_result)
print("Product:", product_result)


# Types of function
# There are two types of function in Python programming:
# 1.Standard library functions - These are built-in functions in Python that are available to use.
# 2.User-defined functions - We can create our own functions based on our requirements.


# python function Arguments

def add_numbers(a, b):
    sum = a + b
    print('sum:', sum)


add_numbers(2, 5)


# Python Keyword Arguments example
def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)


display_info(last_name='Dorothy', first_name='Akoth')


# python recursion-> Function that calls itself

# Example
# This is a recursive function
# to find the factorial of an integer"""
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x - 1))


num = 3
print("The factorial of", num, "is", factorial(num))

# Lambda Functions or Anonymous Function -> a special type of function without function name
"QUIZ CHALLENGE"
"Create a program in python that sort out the length of the  list of the names"
names = ["Jane", "Pauline", "Dorothy", "Akoth"]
names.sort(key=lambda x: len(x))
print(names)

# 1.Example of creating a program of the lambda function

"declare a lambda function"
greet = lambda: print("Hello World")

# call lambda function
greet()


#example:2 Python lambda Function with an Argument

# lambda that accepts one argument
greet_user = lambda name : print('Hey there,', name)

# lambda call
greet_user('Dorothy')


# Based on the scope, we can classify Python variables into three types:
# Local Variables
# Global Variables

# python local variable and global variable

#Global variable
message ="hello"
def greet():
    print(message)

greet()

# Local variable
def greet():
    # local variable
    message = "hello how are you doing?"
    print(message)

greet()

