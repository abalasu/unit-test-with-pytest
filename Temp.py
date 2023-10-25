def multiplier(func):
    def wrapper(*argc, **kwargs):
        print("Function name ", func.__name__)
        print('Function docstring: ' + str(func.__doc__))
        return func(*argc, **kwargs)
    return wrapper

@multiplier 
def doubler(num):
    return num * 2

@multiplier
def tripler(num):
    return num * 3

print(doubler(2))
print(tripler(3))

help(doubler)
help(__doc__)