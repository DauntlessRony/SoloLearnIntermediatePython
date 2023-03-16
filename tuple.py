vTuple1 = 2, 4, 6, 8
vTuple2 = (2, 4, 6, 8)
print(f'vTuple1 = {type(vTuple1)}')
print(f'vTuple2 = {type(vTuple2)}')

numbers = (1, 2, 3)
a, b, c = numbers
print(a)
print(b)
print(c)
a,b = b,a
print(a)
print(b)
print(c)

z = [1, 2]
print(f'type of z {type(z)}')
x, y = [1, 2]
print(f'type of x {type(x)} and type of y {type(y)}')
print(f'value of x {x} and value of y {y}')
x, y = y, x
print(f'value of x {x} and value of y {y}')


a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)

def calc(x):
    # vPerimeter = 4*x
    # vArea = x*x
    p, a = (4*x, x*x)
    return p, a

side = int(input())
p, a = calc(side)

print("Perimeter: " + str(p))
print("Area: " + str(a))

print(range(20))
for i in range(20):
    print(i)
a, b, c, d, *e, f, g = range(20)
print(f'a= {a}')
print(f'b= {b}')
print(f'c= {c}')
print(f'd= {d}')
print(f'e= {e}')
print(f'f= {f}')
print(f'g= {g}')
print(len(e))

nums = (55, 44, 33, 22)
print(nums[:2])
print(min(nums[:2]))
print(max(min(nums[:2]), abs(-42)))




