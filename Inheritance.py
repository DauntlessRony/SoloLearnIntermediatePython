####################################################################
# Start Inheritance

#-------------------------------------------------------------------
# Inheritance
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat(Animal):
    def purr(self):
        print("Purr...")

class Dog(Animal):
    def bark(self):
        print("Woof!")

fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()

#-------------------------------------------------------------------
# Inheritance
class Wolf:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def bark(self):
        print("Grr...")

class Dog(Wolf):
    def bark(self):
        print("Woof")

husky = Dog("Max", "grey")
husky.bark()
#-------------------------------------------------------------------
# Inheritance
class A:
  def method(self):
    print(1)

class B(A):
  def method(self):
    print(2)
print(type(B()))
print(type(B().method()))
B().method()
#-------------------------------------------------------------------
# super_function_call_method_of_super_class
class A:
    def spam(self):
        print('I am from class A.spam')

class B(A):
    def spam(self):
        print('I am from class B.spam')
        super().spam() # this super call spam of class A.

B().spam()

#-------------------------------------------------------------------
# find the area and perimeter:
class Shape:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def area(self):
        print(self.width*self.height)

class Rectangle(Shape):
    def perimeter(self):
        print(2*(self.width+self.height))
# in class Rectangle there have 1. perimeter 2. area (because Shape is inherited to Rectangle class)

w = int(input())
h = int(input())

r = Rectangle(w, h)
r.area()
r.perimeter()
#-------------------------------------------------------------------
# End Inheritance
####################################################################