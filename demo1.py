class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(f'--------------------------')
        print(f'__init__.self.x = {self.x}')
        print(f'__init__.self.y = {self.y}')
        print(f'--------------------------')
    def __add__(self, other):
        print(f'--------------------------')
        print(f'__add__.self.x = {self.x}')
        print(f'__add__.self.y = {self.y} ')
        print(f'--------------------------')
        print(f'__add__.other.x = {other.x} ')
        print(f'__add__.other.y = {other.y} ')
        print(f'##############################')
        return Vector2D(self.x + other.x, self.y + other.y)
        print(f'##############################')
    def __repr__(self):
        return f'Result from __repr__ function: ("{self.x}","{self.y}")'
print(f'=================================================================================')
first = Vector2D(5, 7)
print(f'first = {first}')
print(f'repr(first) = {repr(first)}')
print(f'first.Vector2D(5, 7) = {Vector2D(5, 7)}')
print(f'first.repr(Vector2D(5, 7)) = {repr(Vector2D(5, 7))}')
print(f'=================================================================================')
second = Vector2D(3, 9)
print(f'second = {second}')
print(f'repr(second) = {repr(second)}')
print(f'second.Vector2D(3, 9) = {Vector2D(3, 9)}')
print(f'second.repr(Vector2D(3, 9)) = {repr(Vector2D(3, 9))}')

print(f'=================================================================================')

print(f'Using of repr for first: {repr(first)}')
print(f'Using of repr for second: {repr(second)}')

result = first + second

print(f'Using of repr for result: {repr(result)}')
print(f'=================================================================================')