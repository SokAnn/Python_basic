"""
Декораторы: основы
"""


# function decorator
# manually decorated
def my_decorator(function_to_decorate):
    def wrapper_function():
        print("code before function")
        function_to_decorate()
        print("code after function")
    return wrapper_function


def my_function_to_decorate():
    print("function...")


# standard syntax of decorators
@my_decorator
def another_function_to_decorate():
    print("another function...")


if __name__ == "__main__":
    function_decorated = my_decorator(my_function_to_decorate)
    function_decorated()
    print("\n")
    another_function_to_decorate()
