"""
словари: основы
изменяемые, отображения
"""

# creating
d = {}  # empty
print(d, type(d))
# key must be immutable data type: number, string, tuple
d1 = {'dict': 1, 'dictionary': 2}
print(d1)
d2 = dict(first='dict', second='dictionary')
print(d2)
d3 = dict.fromkeys(['a', 'b'], 5)
print(d3)
d4 = {i: i ** 2 for i in range(1, 11)}  # dictionary generator
print(d4)
key_list = [1, 2, 3]
value_list = ["cat", "dog", "mouse"]
d5 = dict(zip(key_list, value_list))
print(d5)
print("-------------")

# operators
print("operator in : ", (1 in d5, "dog" in d5))
print(d5[2])  # dict[key] -> value
print(d2["first"])

# built-in functions
print("length: ", len(d5))
print("key sort: ", sorted(d5))  # key sort
# dict()
print("-------------")

# methods
d1.clear()  # clear()
print("clear() method: ", d1)

some_dict = d4.copy()  # copy()
print("copy() method: ", some_dict)

# fromkeys()

print("get() method: ", d5.get(1, "There is no value for this key!"))  # get()
print("get() method: ", d5.get(6, "There is no value for this key!"))

print("items() method: ", d5.items())  # items()
print("keys() method: ", d5.keys())  # keys()

print("pop() method: ", d2.pop("first"))  # pop()
print(d2)

print("popitem() method: ", d4.popitem())  # popitem()
print(d4)

print("setdefault() method: ", d4.setdefault(3))  # setdefault()
print("setdefault() method: ", d4.setdefault(20))
print("setdefault() method: ", d4.setdefault(21, 441))
print(d4)

d5.update(d3)  # update()
print("update() method: ", d5)

print("values() method: ", d5.values())  # values()
print("-------------")

# update or add element(s)
print("update or add element(s):")
print(d5)
d5["a"] = "str"
print(d5)

# removal element(s)
print("removal element(s):")
print(d5)
del d5["a"]
print(d5)
