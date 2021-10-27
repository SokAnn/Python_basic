"""
кортежи: основы
неизменяемые, последовательности
"""

# creating
t = tuple()  # empty
print(t, type(t))
t1 = ()  # empty
print(t1, type(t1))
t2 = ("s",)  # tuple of one element!
print(t2, type(t2))
t3 = "s",
print(t3, type(t3))
t4 = tuple("string")
print(t4, type(t4))
t5 = (1, 2, 3, 4, 5, 6, 7)
print(t5, type(t5))
t6 = (3, "24", 3, 4, [5, "ae", 1.4], 6, "abf", 1.6, {1: 1, 2: 4, 3: 9})
print(t6, type(t6))
print("-------------")

# operators
print("index: ", t6[4])
print("slice: ", t5[1:5])
print("operator + (concatenate): ", t3 + t4)
print("operator * (repeat):", t5 * 2)
print("operator < :",  (1, 2, 3) < t5)
print("operator > :",  (1, 2, 3) > t5)
print("operator <= :",  (1, 2, 3, 4) <= t5)
print("operator >= :",  (1, 2, 3, 4) >= t5)
print("operator == :",  (1, 2, 3, 4, 5, 6, 7) == t5)
print("operator != :",  t6 != t5)
print("operator in :", 3 in t5)
print("-------------")

# built-in functions
print("length: ", len(t6))
print("sorted: ", tuple(sorted((3, 6, 1, 9, 4))))
print("min: ", min(t5))
print("max: ", max(t5))
print("sum: ", sum(t5))  # works only with numeric types
print("any: ", any(t5))
print("-------------")
# tuple()

# methods
print("index() method: ", t6.index("24"))  # index()
print("count() method: ", t6.count(3))  # count()

# removal all elements
del t4
