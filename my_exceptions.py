"""
исключения: основы
"""


# try-except
def func_with_exception_zero_div(a, b):
    try:
        result = a / b
        return result
    except Exception:  # except ZerodivisionError: - best way; except Exception: - too broad exception clauses
        print('\tZerodivisionError!!!')
        return "ZerodivisionError"


# try-except/else
def func_with_exception(a):
    try:
        mas = [1, 2, 3, 4, 5]
        result = mas[a]
    except IndexError:
        print('\tIndexError!!!')
        return "IndexError"
    else:
        print('\tno errors')
        return result


# try-except/finally
# try-except/else/finally


if __name__ == "__main__":
    print('construction try-except')
    res1 = func_with_exception_zero_div(10, 5)
    res2 = func_with_exception_zero_div(10, 0)
    print(f'results of functions:\n\tfunction 1 = {res1}\n\tfunction 2 = {res2}\n')

    print('construction try-except/else')
    res1 = func_with_exception(2)
    res2 = func_with_exception(10)
    print(f'results of functions:\n\tfunction 1 = {res1}\n\tfunction 2 = {res2}')

    print('')
