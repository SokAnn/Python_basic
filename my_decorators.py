"""
Декораторы: основы
"""


# function decorator
# manually decorated
def my_decorator(function_to_decorate):
    def wrapper_function():  # function without arguments
        print("code before function")
        function_to_decorate()
        print("code after function")
    return wrapper_function


def my_function_to_decorate():  # function without arguments
    print("function without arguments...")


def my_decorator_args(function_to_decorate):
    def wrapper_function_with_args(arg1, arg2, arg3):  # function with arguments
        print("passed arguments: ", (arg1, arg2, arg3))
        function_to_decorate(arg1, arg2, arg3)
    return wrapper_function_with_args


def my_function_to_decorate_args(arg1, arg2, arg3):  # function with arguments
    print(f"function with arguments... {arg1, arg2, arg3}")


# standard syntax of decorators
@my_decorator
def another_function_to_decorate():
    print("another function...")


@my_decorator_args
def another_function_to_decorate_args(first_name, last_name, age):
    print("another function with arguments...")
    print(f"First name: {first_name}\tLast name: {last_name}\tAge: {age}")


if __name__ == "__main__":
    function_decorated = my_decorator(my_function_to_decorate)
    function_decorated()
    print("\n")
    another_function_to_decorate()
    print("\n")

    function_decorated_args = my_decorator_args(my_function_to_decorate_args)
    function_decorated_args("Ivan", "Ivanov", 25)
    print("\n")
    another_function_to_decorate_args("Ivan", "Ivanov", 25)
