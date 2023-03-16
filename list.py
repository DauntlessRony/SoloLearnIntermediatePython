vList = [2, 4, 6, 8]
print(type(vList))
print(vList[1])
print(vList[1:3])
print(vList[-3:-1])
print(vList[-1])
print(vList[-3])
print(vList[:])
print(vList+vList)

vList = [2, 4, 6, 8]
print(vList)
vList[1] = 10
print(vList)
vList[1] = 4
vList.append(10)
print(vList)
print(len(vList))

vL1 = [1,2,3,4]
vL2 = [5,6,7,8]
vL3= [vL1,vL2]
print(vL3)
print(vL3[0])
print(vL3[1])
print(vL3[0][2])
print(vL3[1][3])


# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(f'a =  {a}')
    print(f'b =  {b}')
    a, b = b, a+b


# a list comprehension
cubes = [i**3 for i in range(5)]
print(type(cubes))
print(cubes)

print([i*2 for i in range(10)])

evens1=[i**2 for i in range(10)]
print(evens1)
evens=[i**2 for i in range(10) if i**2 % 2 == 0]
print(evens)

word = 'awesome'
# print(word)
# vList = list(word)
# print(vList)
evens=[i for i in word if i not in 'aeiou']
print(evens)

print([i for i in range(20) if i%3 == 0])
