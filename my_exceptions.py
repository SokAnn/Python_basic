"""
исключения: основы
"""


# try/except
def func_with_exception_zero_div(a, b):
    # an exception may appear inside this block
    try:
        result = a / b
        return result
    # the code that should be executed when an error occurs
    except Exception:  # except ZerodivisionError: - best way; except Exception: - too broad exception clauses
        print('\tZerodivisionError!!!')
        return "ZerodivisionError"


# try/except/else
def func_with_exception_ind_err(a):
    try:
        mas = [1, 2, 3, 4, 5]
        result = mas[a]
    except IndexError:
        print('\tIndexError!!!')
        return "IndexError"
    # the code is executed if there were no errors
    else:
        print('\tno errors')
        return result


# try/finally
def func_exc_fin(file_name):
    file = open(file_name, 'r')
    print('\tfile was opened...')
    try:
        lines = file.readlines()
        print('\t', lines[0:])
    # the code that is executed at the conclusion of the work (it does not matter if there was an error or not)
    # it is usually used to close files, for example (for files, it is better to use with/as construction)
    finally:
        file.close()
        print('\tfile was closed...')


# try/except/finally
def func_with_exception_fin(a):
    try:
        mas = [1, 2, 3, 4, 5]
        return mas[a]
    except IndexError:
        print('\tIndexError!!!')
        return "IndexError"
    finally:
        print('\tfinally')


# try/except/else/finally
def func_with_exception_ef(a):
    try:
        mas = [1, 2, 3, 4, 5]
        res = mas[a]
    except IndexError as err:  # as saves the error as a variable for further access to it
        print('\t', err)
    else:
        print('\telse')
    finally:
        print('\tfinally')


# try/except with several except-blocks
def excs_division():
    a = input('\ta = ')
    b = input('\tb = ')
    try:
       res = float(a) / float(b)
    except ZeroDivisionError:
        print('ZeroDivisionError')
    except ValueError:
        print('ValueError')
    else:
        print(res)


# try/except with several except in one
def exc_division():
    a = input('\ta = ')
    b = input('\tb = ')
    try:
       res = float(a) / float(b)
    except (ZeroDivisionError, ValueError) as err:
        print(err)
    else:
        print(res)


# raise
def func_raise(var_max):
    try:
        if var_max < 500:
            # forcing an exception call
            raise Exception('max must be more than 500')
    except Exception as exc:
        print('\tmistake!!!')
        print('\tException: ', exc)
    else:
        print('\tno errors...')


# assert
def func_assert(var):
    try:
        # syntax: condition, message (optional) under false condition
        assert var != 0, 'variable must be True value'
    except AssertionError:
        print('\tAssertionError')
    else:
        print('\tno errors...')


if __name__ == "__main__":
    print('construction try/except:')
    print('without error:')
    func_with_exception_zero_div(10, 5)
    print('with error:')
    func_with_exception_zero_div(10, 0)

    print('\nconstruction try/except/else:')
    print('without error:')
    func_with_exception_ind_err(2)
    print('with error:')
    func_with_exception_ind_err(10)

    print('\nconstruction try/finally:')
    print('results of function (without error):')
    func_exc_fin("file.txt")

    print('\nconstruction try/except/finally:')
    print('without error:')
    func_with_exception_fin(2)
    print('with error:')
    func_with_exception_fin(10)

    print('\nconstruction try/except/else/finally:')
    print('without error:')
    func_with_exception_ef(2)
    print('with error:')
    func_with_exception_ef(10)

    print('\nconstruction try/except with several except-blocks:')
    excs_division()

    print('\nconstruction try/except with several except in one:')
    exc_division()

    print('\noperator raise:')
    print('without error:')
    func_raise(1000)
    print('with error:')
    func_raise(100)

    print('\noperator assert:')
    print('without error:')
    func_assert(1)
    print('with error:')
    func_assert(0)
