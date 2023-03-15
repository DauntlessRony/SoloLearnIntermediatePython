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