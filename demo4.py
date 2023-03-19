def double(f):
    print(type(f))
    def aux(*xs, **kws):
        print(type(xs))
        print(type(kws))
        return 2 * f(*xs, **kws)
    return aux

@double
def function(a):
    return 10 + a

print (function(3)) # Prints 26, namely 2 * (10 + 3)