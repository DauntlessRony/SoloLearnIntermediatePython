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
# Start Lambdas



# End Lambdas
####################################################################
####################################################################