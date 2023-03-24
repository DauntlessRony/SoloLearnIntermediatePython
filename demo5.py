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