# return ((num % 2) + (10 * convert(num // 2)))
print(0 % 2) # 0
print(0 // 2) # 0
#1. return ((2 % 2) + (10 * convert(2 // 2))) # n = 2
#1. return ((0) + (10 * convert(1))) # n = 1
#2. return ((1 % 2) + (10 * convert(1 // 2)))  # n = 1
#2. return ((1) + (10 * convert(0))) # n = 0
#3. return ((0 % 2) + (10 * convert(0 // 2))) # n = 0
#3. return 0 # n = 0