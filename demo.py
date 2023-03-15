#
contacts = [
    ('James', 42),
    ('Amy', 24),
    ('John', 31),
    ('Amanda', 63),
    ('Bob', 18)
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

vInput = input()
if vInput in contacts:
    for i in vInput:
        print(f'{i[0]} is {i[1]}')
        break
else:
    print('Not Found')
    break
