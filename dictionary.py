vDictionary = {1:2, 2:4, 3:6, 4:8}
print(f'vDictionary = {type(vDictionary)}')
print(vDictionary)

data = {
    'Singapore': 1,
    'Ireland': 6,
    'United Kingdom': 7,
    'Germany': 27,
    'Armenia': 34,
    'United States': 17,
    'Canada': 9,
    'Italy': 74
}
print(data.get('Ireland','Not found'))
print(data.get('Irelandc','Not found'))
# print(data.get(input(),'Not found'))

fib = {1: 1, 2: 1, 3: 2, 4: 3}
print(fib.get(4, 0) + fib.get(7, 5))
print(3+5)

#--------------------
#
contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18),
    ('x', 20)
]
# print(type(contacts))
# print(type(contacts[1]))
# print(contacts[1])
#
# vInput = input()
# vTupleIndexKey = 0
# vTupleIndexValue = 1
# for i in contacts:
#     print(i)
#     print(type(i))
#     print(vTupleIndexKey)
#     print(vTupleIndexValue)
#     print(type(i[vTupleIndexKey]))
#     print(type(i[vTupleIndexValue]))
#     print(i[vTupleIndexKey])
#     print(i[vTupleIndexValue])
#     print(f'{i[vTupleIndexKey]} is {i[vTupleIndexValue]}')

# vInput = input()
# for i in contacts:
#     if vInput in i:
#         print(f'{i[0]} is {i[1]}')
#         break
#     else:
#         print('Not Found')
#         break

# vInput = input()
# if vInput in contacts:
#     for i in vInput:
#         print(f'{i[0]} is {i[1]}')
#         break
# else:
#     print('Not Found')
#     break

vInput = input()
for i in contacts:
    if i[0] == vInput:
        print(f'{i[0]} is {i[1]}')
        break
else:
    print('Not Found')


# vName = input()
# for i in contacts:
#     if i[0] == vName:
#         print(vName, "is", i[1])
#         break
#     else:
#         print('Not Found')

#--------------------

text = 'hello'
dict = {}
for t in text:
    dict[t] = text.count(t)
print(dict)

