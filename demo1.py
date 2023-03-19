# *args and **kwargs
# *args
# Do not understand 'The parameter *args must come after the named parameters to a function.'
def function(*args):
    # print(named_arg)
    print(args)

function(1, 2, 3, 4, 5)

# **kwargs