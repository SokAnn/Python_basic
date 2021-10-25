"""
числа: основы
неизменяемые
целые/с плавающей точкой/комплексные
расширение: десятичные с фиксированной точностью/рациональные
"""

import math
from decimal import *
from fractions import *

# creating - создание
int_1 = 5
float_1 = 5.0
complex_1 = 5 + 6j
complex_2 = complex(1, 2)
var = 1_000_000

# type definition - определение типа
print("value = ", int_1, "\ttype: ", type(int_1))
print("value = ", float_1, "\ttype: ", type(float_1))
print("value = ", complex_1, "\ttype: ", type(complex_1))
print("value = ", complex_2, "\ttype: ", type(complex_2))
print("value = ", var, "\ttype: ", type(var))
print(isinstance(int_1, int), isinstance(int_1, float), isinstance(int_1, complex))
print("-------------")

# arithmetic operations - арифметические операции
print("sum:", (int_1 + 2, float_1 + 10.0, complex_1 + 1 + 3j))
print("sub:", (int_1 - 2, float_1 - 1.7, complex_1 - 10 - 1j))
print("mul:", (int_1 * 2, float_1 * 8.1, complex_1 * (2 - 4j)))
print("exp:", (int_1 ** 2, float_1 ** 3, complex_1 ** 2))
print("div:", (int_1 / 2, float_1 / 2.5, complex_1 / (1 - 1j)))
# complex numbers doesn't define // and %
print("div:", (int_1 // 2, float_1 // 2.5))
print("div:", (int_1 % 2, float_1 % 2.5))
print("-------------")

# bitwise operations - побитовые операции
print("bitwise or:", int_1 | int_1)
print("bitwise and:", int_1 & int_1)
print("exc or:", int_1 ^ int_1)
print("shift left:", int_1 << 2)
print("shift right:", int_1 >> 2)
print("bitwise not:", ~ int_1)
print("-------------")

# comparison operations - операции сравнения
print("less:", int_1 < int_1)  # int, float
print("more:", int_1 > int_1)  # int, float
print("less or equal:", int_1 <= int_1)  # int, float
print("more or equal:", int_1 >= int_1)  # int, float
print("equal:", int_1 == int_1)  # int, float, complex
print("not equal:", int_1 != int_1)  # int, float, complex
print("-------------")

# built-in functions - встроенные функции
print(pow(10, 2), pow(15, 3))  # equal 10 ** 2 and 15 ** 3
print(abs(-15), abs(42))
print(round(1.49), round(5.5), round(10.51))  # not for complex numbers
# mathematical module - math
print(math.trunc(1.49), math.trunc(5.5), math.trunc(10.51), math.trunc(-5.4))  # cutting off the whole part
print(math.floor(1.49), math.floor(5.5), math.floor(10.51), math.floor(-5.4))  # rounding downwards
print("-------------")

# int: hex(), oct(), bin(), int(), int.bit_length(), int.to_bytes(), int.from_bytes()
print(hex(189), hex(-189), type(hex(189)))
print(oct(57), oct(-57), type(oct(57)))
print(bin(37), bin(-37), type(bin(37)))
print(int('0b100101', 2), int('0o71', 8), int('0xbd', 16))
print("number of bits:", int_1.bit_length())
print("int -> byte string:", int_1.to_bytes(2, byteorder='big'))
print("byte string -> int:", int.from_bytes(b'\x00\x05', byteorder='big'))
print("-------------")

# float: float.is_integer(), float.hex(), float.as_integer_ratio()
print("is integer?", (float_1.is_integer(), 25.45.is_integer()))
print("float in hex:", (float_1, float_1.hex()))
print("as ratio:", float_1.as_integer_ratio())
print("-------------")

# complex: c.conjugate(), c.imag, c.real,
print("conjugate:", (complex_1.conjugate(), complex_2.conjugate()))
print("imaginary part:", (complex_1.imag, complex_2.imag))
print("real part:", (complex_1.real, complex_2.real))
print("-------------")

# type conversion - преобразование типов
print("float -> int:", int(float_1))
print("int -> float:", float(int_1))
print("int -> complex:", complex(int_1))
print("-------------")

# Decimal и Fraction расширения
print(0.1 + 0.2)  # result = 0.30000000000000004 -> error?
print(getcontext())  # show basic parameters
getcontext().prec = 6  # set new parameter
number1 = Decimal(0.1)
number2 = Decimal(0.2)
print(number1 + number2)
print(Fraction(16, -10))
print(Fraction(33.33))
print(Fraction("33.33"))
