"""
функции: основы
"""

# return value
# function returns some value (no None)
def add(a, b, c):
    return a + b + c

# function returns None value (by default)
def show(a, b):
    str_a = str(a)
    str_b = str(b)

# def

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

#
def func4(*args):
    return args

#
def func5(**kwargs):
    return kwargs

#
# def

if __name__ == "__main__":
    # examples: return value
    res = add(1, 2, 3)
    print("add() result = ", res)
    print(show(1, 2))
    f = func(2)
    print(f(5))
    # examples: arguments
    func1()
    func2(6, 9)
    func3(16, 4)
    func3(9, 8, 7)
    print(func4(1, 2, "kek", [20, 5], {'a': 1, 'b': 2}, (5, 7, 6)))
    print(func5(a=1, b=2, c=3, d=4))
