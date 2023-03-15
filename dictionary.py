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