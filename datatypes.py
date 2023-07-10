# INTRODUCTION TO LIST
# lists are collection of an ordered items

# To access individual of a list we use indexes

# for example
Languages = ["Python", "Java", "Kotlin", "JavaScript", "C++"]
print(Languages[2])

# To access a portion of alist, we use the slicing operator
Languages = ["Python", "Java", "Kotlin", "JavaScript", "C++"]
print(Languages[0:3])

# We can also use loops to iterate through a list
Languages = ["Python", "Java", "Kotlin", "JavaScript", "C++"]
for language in Languages:
    print(language)

# STRING
# string is a sequence of characters
# to create strings we can use double quotes or single quotes
text = "Dorothy"
print(text)
# Or
t = 'home'
# To access an individual character from a list we use indices
print(text[2])

# To access a substring from a list we use the slicing operator
print(text[:4])

# A string is a sequence and we can iterate through characters of a string using a loop
for characters in text:
    print(characters)

# Strings are immutable
text = 'Dorothy'
# message[0] = 'a'
# print(message)

# QUIZ CHALLENGE/Task
quote = "Talk is cheap . Show me the code"
print("1.", quote[3])

print("2", quote[-3])

print("3.", quote.replace("code", "program"))

# DICTIONARIES
# dictionaries uses curly braces
# A dictionary is a compound data type that allows us to work with key pair values
# we can create dictionaries like this:
country_code = {"United States": +49, "Kenya": 254, "Nigeria": 234}
print(country_code)

# We can easily access a value from a dictionary if it's key is known
print(country_code["United States"])

# To add / change items from a dictionary ,


# we can assign values to the keys

# we can remove a specified items from a dictionary by using the pop() method
country_code.pop("Kenya")
print(country_code)

# we can iterate through a dictionary using a for-loop
for country in country_code:
    print(country)

# to remove items completely in dictionary we use clear
# Example:
country_code = {
    "United States": +49, "Kenya": 254, "Nigeria": 234
}
country_code.clear()

print(country_code)

# What is the output of the following

mixed_list = ["Hello", -34, "Java", True]
print("1.", mixed_list[-1])

mixed_list[1] = "Hi"
print("2", mixed_list)

mixed_tuple = (1, 3, 4, 5)
# tuple objects does not support item assignment
# mixed_tuple[1]=100
# print("3",mixed_tuple)


# Sets in Python -> Are collection of unique data
# Sets uses curly braces
# example
animals = {"Dog","Cat", "Cow", "Camel"}
print(animals)

# A set cannot use duplicate items and all the sets items must be immutable
# we can  add and remove items from sets
# Set items are mutable but Sets are mutable
#

