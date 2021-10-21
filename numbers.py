'''
числа: основы
неизменяемые
целые/с плавающей точкой/комплексные
расширение: десятичные с фиксированной точностью/рациональные
'''

# создание
int_1 = 5
float_1 = 5.0
complex_1 = 5 + 6j
var = 1_000_000

# type definition - определение типа
print("value = ", int_1, "\ttype: ", type(int_1))
print("value = ", float_1, "\ttype: ", type(float_1))
print("value = ", complex_1, "\ttype: ", type(complex_1))
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
print("less:", int_1 < int_1)
print("more:", int_1 > int_1)
print("less or equal:", int_1 <= int_1)
print("more or equal:", int_1 >= int_1)
print("equal:", int_1 == int_1)
print("not equal:", int_1 != int_1)
print("-------------")

# built-in functions - встроенные функции
print(pow(10, 2), pow(15, 3))  # equal 10 ** 2 and 15 ** 3
print(abs(-15), abs(42))
print(round(1.49), round(5.5), round(10.51))
print(hex(189), hex(-189), type(hex(189)))
print(oct(57), oct(-57), type(oct(57)))
print(bin(37), bin(-37), type(bin(37)))
print(int('0b100101', 2), int('0o71', 8), int('0xbd', 16))
print("number of bits:", int_1.bit_length())
print("byte string:", int_1.to_bytes(2, byteorder='big'))
print("-------------")

# type conversion - преобразование типов
print("float -> int:", int(float_1))
print("int -> float:", float(int_1))
print("int -> complex:", complex(int_1))
