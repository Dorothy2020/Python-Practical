class Student:
    def check_pass_fail(self):
        if self.marks >= 50:
            return True

        else:
            return False


# creating objects
student1 = Student()
student1.name = "Dotty"
student1.marks = 30

did_pass = student1.check_pass_fail()

print(did_pass)


# Python Inheritance
class Animal:
    # attribute and method of the parent class
    name = ""

    def eat(self):
        print("I can eat")


# inherit from Animal
class Dog(Animal):

    # new method in subclass
    def display(self):
        # access name attribute of superclass using self
        print("My name is ", self.name)


# create an object of the subclass
labrador = Dog()

# access superclass attribute and method
labrador.name = "Rohu"
labrador.eat()

# call subclass method
labrador.display()

#In Python, inheritance is an is-a relationship
#That is, we use inheritance only if there exists an is-a relationship between two classes

#A polygon is a closed figure with 3 or more
#sides. Say, we have a class called Polygon defined as follows,
class Polygon:
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])


#A triangle is a Polygon with 3 sides.So,
# we can create a class called Triangle which inherits from Polygon.
# This makes all the attributes of Polygon class available to the Triangle class.

class Triangle(Polygon):
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a, b, c = self.sides
        # calculate the semi-perimeter
        s = (a + b + c) / 2
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)



class Polygon:
    # Initializing the number of sides
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    # method to display the length of each side of the polygon
    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Triangle(Polygon):
    # Initializing the number of sides of the triangle to 3 by
    # calling the __init__ method of the Polygon class
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a, b, c = self.sides

        # calculate the semi-perimeter
        s = (a + b + c) / 2

        # Using Heron's formula to calculate the area of the triangle
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

# Creating an instance of the Triangle class
t = Triangle()

# Prompting the user to enter the sides of the triangle
t.inputSides()

# Displaying the sides of the triangle
t.dispSides()

# Calculating and printing the area of the triangle
t.findArea()


# method overriding
class Animal:
    # attributes and method of the parent class
    new = ""
    def eat(self):
        print("I can eat")


# inherit from Animal
class Dog(Animal):

    # override eat() method
    def eat(self):
        print("I like to eat bones")


# create an object of the subclass
labrador = Dog()

# call the eat() method on the labrador object
labrador.eat()

class Polygon:
    # Initializing the number of sides
    def __init__(self, no_of_sides):
        self.n = no_of_sides
        self.sides = [0 for i in range(no_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.n)]

    # method to display the length of each side of the polygon
    def dispSides(self):
        for i in range(self.n):
            print("Side",i+1,"is",self.sides[i])

class Triangle(Polygon):
    # Initializing the number of sides of the triangle to 3 by
    # calling the __init__ method of the Polygon class
    def __init__(self):
        Polygon.__init__(self,3)

    def findArea(self):
        a, b, c = self.sides

        # calculate the semi-perimeter
        s = (a + b + c) / 2

        # Using Heron's formula to calculate the area of the triangle
        area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
        print('The area of the triangle is %0.2f' %area)

# Creating an instance of the Triangle class
t = Triangle()

# Prompting the user to enter the sides of the triangle
t.inputSides()

# Displaying the sides of the triangle
t.dispSides()

# Calculating and printing the area of the triangle
t.findArea()


# method overriding
class Animal:
    # attributes and method of the parent class
    name = ""

    def eat(self):
        print("I can eat")


# inherit from Animal
class Dog(Animal):

    # override eat() method
    def eat(self):
        print("I like to eat bones")


# create an object of the subclass
labrador = Dog()

# call the eat() method on the labrador object
labrador.eat()

# The super() Method in Python Inheritance
class Animal:
    name = ""

    def eat(self):
        print("I can eat")


# inherit from Animal
class Dog(Animal):

    # override eat() method
    def eat(self):
        # call the eat() method of the superclass using super()
        super().eat()

        print("I like to eat bones")


# create an object of the subclass
labrador = Dog()

labrador.eat()