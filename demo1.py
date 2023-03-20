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
    return 'HI'
my_min(8, 13, 4, 42, 120, 7)