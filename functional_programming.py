####################################################################
####################################################################
# Start Functional Programming
#-------------------------------------------------------------------
def apply_twice(func, arg): # func = add_five function and arg = 10 for the first call
    return func(func(arg))  # func(arg) = add_five(10); so, it goes to add_five function and return 15
                            # and lastly func(func(arg)) = func(15); and it goes to add_finction and return 20
def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))
#-------------------------------------------------------------------
def test(func, arg):
  return func(func(arg))

def mult(x):
  return x * x

print(test(mult, 2))
#-------------------------------------------------------------------
def pure_function(x, y):
  temp = x + 2*y
  print(temp)
  temp2 = 2*x + y
  print(temp2)
  return temp / temp2

print(pure_function(2, 3))

some_list = []

def impure(arg):
  some_list.append(arg)

impure(range(12))
print(some_list)
#-------------------------------------------------------------------
def func(x):
  y = x**2
  z = x + y
  return z

#-------------------------------------------------------------------
nums = (55, 44, 33, 22)
print(max(min(nums[:2]), abs(-42)))
#-------------------------------------------------------------------
n = [2, 4, 6, 8]
res = 1
for x in n[1:3]:
  res *= x

print(res)
# End Functional Programming
#-------------------------------------------------------------------
####################################################################
####################################################################
# Start Lambda

price = int(input())
perc = int(input())

res = (lambda x,y:(y/100)*x)(price, perc)

print(res)


# End Lambda
####################################################################
####################################################################
# Start map & filter
def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)
# End map & filter
####################################################################
####################################################################
# Start Generators

# return vs yield
# yield
def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1

for i in countdown(): # in that position, for loop access the local variable of coundown function;
    print(f' using yield {i}')

def countdown():
    i=5
    while i > 0:
        print(f' using return {i}')
        i -= 1
    return i

countdown() # if we use return, we cannot access the local variable from other functions;


def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i
for i in numbers(11):
    print(i)
print(list(numbers(11)))

# End Generators
####################################################################
####################################################################
# Start prime numbers

# prime numbers
def isPrime(x):
    if x < 2:
        return False
    elif x == 2:
        return True
    for n in range(2, x):
        if x % n ==0:
            return False
    return True

def primeGenerator(a, b):
    for i in range(a,b):
        print(f'The value of i inside for loop {i}.')
        if isPrime(i):
            print(f'The value of i after isPrime call {i}.')
            print(f'The value of i before yield call {i}.')
            yield i
            print(f'The value of i after yield call {i}.')
            i +=1

# f = int(input())
# t = int(input())

print(list(primeGenerator(10, 20)))

def make_word():
  word = ""
  for ch in "spam":
    word +=ch
    print(f'before yield = {word}')
    yield word
    print(f'after yield = {word}')

f = list(make_word())
print(f)

# End prime numbers
####################################################################
####################################################################
# Start Decorators
# Decorators
def decor(func):
    def wrap():
        print("============")
        func()
        print("============")

    return wrap


def print_text():
    print("Hello world!")


decorated = decor(print_text)
decorated()


# explicitly call vs implicitly call a decor function
def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def print_text():
    print("Hello world!")

print_text = decor(print_text)

print_text();

# or

def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

@decor
def print_text():
    print("Hello world!")

print_text();

def decor(func):
    def wrap(v):
        print("***")
        func(v)
        print("***")
    return wrap

@decor
def invoice(v):
    print(f'INVOICE # {v}')

v = '10'
print(type(v))
invoice(v)

def decor(func):
    def wrap(*t, **d):
        print("***")
        func(*t, **d)
        print("***")
    return wrap

@decor
def invoice(v):
    print(f'INVOICE # {v}')

v = '10'
print(type(v))
invoice(v)


# End Decorators
####################################################################
####################################################################
# Start Recursion

# Recursion
# Recursion Behave of function
def factorial(x):
    if x == 1:
        return 1
    else:
        print(f'The factorial Function call = {x}')
        return x * factorial(x-1)
        # 1. x = 5; 5 * factorial(4)
                        # 2. x = 4; 4 * factorial(3)
                                        # 3. x = 3; 3 * factorial(2)
                                                        # 4. x = 2; 2 * factorial(1)
# ------Recursively factorial function call ; Result = 120;
print(factorial(5))


def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)
def is_odd(x):
    return not is_even(x)

print(is_odd(17))
print(is_even(23))

# Decimal to Binary
def convert(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return ((num % 2) + (10 * convert(num // 2)))

print(convert(int(input())))

def fib(x):
  if x == 0 or x == 1:
    return 1
  else:
    return fib(x-1) + fib(x-2)
  #             3           2
  #          2    1       1    0
  #        1  0   1       1    1
  #        1  1   1       1    1
print(fib(4))

# End Recursion
####################################################################
####################################################################
# Start *args and **kwargs

# *args and **kwargs
# *args
# Do not understand 'The parameter *args must come after the named parameters to a function.'
def function(*args):
    # print(named_arg)
    print(args)

function(1, 2, 3, 4, 5)

# **kwargs

def my_func(x, y=7, *args, **kwargs):
    print(kwargs)

my_func(2, 3, 4, 5, 6, a=7, b=8)

# End *args and **kwargs
####################################################################
####################################################################
# Start codeA

#-------------------------------------------------------------------
# take any number of variables and find the min
def my_min(*args):
    print(f'type of args {type(args)}')
    print(f'value of args {args}')
    min = args[0]
    vIndex = 0
    for i in args:
        print(f'value of args[{vIndex}] = {i}')
        print(args[vIndex])
        print(min)
        if args[vIndex] < min:
            min = args[vIndex]
        print(args[vIndex])
        print(min)
        vIndex += 1
    return min
print(my_min(8, 13, 4, 42, 120, 7))
#-------------------------------------------------------------------
nums = {1, 2, 3, 4, 5, 6}
nums = {0, 1, 2, 3} & nums
nums = filter(lambda x: x > 1, nums)
print(len(list(nums)))
#-------------------------------------------------------------------
def power(x, y):
  if y == 0:
    return 1
  else:
    return x * power(x, y-1)
  # 2 * power(2,2)
        # 2 * power(2,1)
              # 2 * power(2,0)
                    # 1
  # 2 * 2 * 2 * 1
        # 2 * 2 * 1
              # 2 * 1
                    # 1
print(power(2, 3))
#-------------------------------------------------------------------
nums = [1, 2, 8, 3, 7]

res = list(filter(lambda x: x%2 == 0, nums))
print(res)
#-------------------------------------------------------------------
def func(**kwargs):
  print(kwargs["zero"]) # key = zero and value = 8

func(a = 0, zero = 8)
#-------------------------------------------------------------------
def spell(txt):
    print(txt)
    print(type(txt))
    print(len(txt))
    vIndex = len(txt)-1
    for i in txt:
        print(vIndex)
        print(txt[vIndex])
        vIndex -= 1

txt = 'HELLO'
spell(txt)

#-------------------------------------------------------------------
def spell(txt):
    vIndex = len(txt)-1
    for i in txt:
        print(txt[vIndex])
        vIndex -= 1

txt = 'HELLO'
spell(txt)

#-------------------------------------------------------------------


# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################
####################################################################
# Start codeA



# End codeA
####################################################################