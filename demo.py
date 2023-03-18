# prime numbers
def isPrime(x):
    if x < 2:
        return False
        print(f'{x} is not a prime number.')
    elif x == 2:
        return True
        print(f'{x} is a prime number.')
    for n in range(2, x):
        if x % n ==0:
            return False
            print(f'{x} is not a prime number.')
    return True
    print(f'{x} is a prime number.')

def primeGenerator(a, b):
    for i in range(a,b):
        print(f'The value of i before yield call {i}.')
        #yield i
        print(f'The value of i after yield call {i}.')
        print(isPrime(i))
        print(f'The value of i after call isPrime{i}.')
        i += 1

# f = int(input())
# t = int(input())

# print(list(primeGenerator(f, t)))
primeGenerator(10, 20)
