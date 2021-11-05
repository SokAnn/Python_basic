"""
функции: основы
"""


# return value
# function returns some value (no None)
def add(a, b, c):
    return a + b + c

# function returns None value (by default) if function do not have operator return
def show(a, b):
    str_a = str(a)
    str_b = str(b)

# function can return several values
def return_values(a, b, c):
    return a, b, c  # returns a tuple

# function can return function object (function can return any type of object!)
def func(x):
    def myfunc(n):
        return x ** n
    return myfunc


# parameters - arguments
# function may not accept arguments
def func1():
    print("Hello world!!!")

# positional arguments (mandatory)
def func2(a, b):
    print(f"a = {a}\tb = {b}")

# optional arguments (standard value by default)
def func3(a, b, c=0):
    print(f"a = {a}\tb = {b}\tc = {c}")

# number of positional arguments is variable: args = tuple
def func4(*args):
    return args

# number of named arguments is variable: kargs = dictionary
def func5(**kwargs):
    return kwargs

# annotation of types
def my_pow(a: int, b:int) -> int:
    return a ** b

# recursive function
def Fibonacci(n):
    if n <= 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)

# generator function
def my_gen(p):
    for i in range(p):
        yield i ** 2


if __name__ == "__main__":
    # examples: return value
    res = add(1, 2, 3)
    print("add() result = ", res)
    print(show(1, 2))
    print(return_values('a', 'b', 'c'), type(return_values('a', 'b', 'c')))
    a, b, c = return_values('a', 'b', 'c')  # unpacking: the number of variables on the left should equal the number of variables on the right
    f = func(2)
    print(f(5))

    # examples: arguments
    func1()
    func2(6, 9)
    func2(b=10, a=5)  # named arguments
    func3(16, 4)
    func3(9, 8, 7)
    print(func4(1, 2, "kek", [20, 5], {'a': 1, 'b': 2}, (5, 7, 6)))
    print(func5(a=1, b=2, c=3, d=4))
    res = my_pow(1, 2)
    # res = my_pow(1.0, 2)  # error: arguments must be int values
    n = 5
    print(f"Fibonacci n = {n}: ", Fibonacci(n))
    n = 7
    print(f"Fibonacci n = {n}: ", Fibonacci(n))

    # lambda functions:
    power = lambda x, y: x ** y
    x = 2
    y = 5
    print(f"lambda x = {x}, y = {y}: ", power(x, y))

    # generator functions & generators
    # function - my_gen()
    print("generator functions: ")
    for i in my_gen(10):
        print(i, end=' ')
    print("\ngenerator expression: ")
    # generator
    g = (i ** 2 for i in range(10))
    for i in g:
        print(i, end=' ')
