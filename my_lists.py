"""
списки: основы
изменяемые, последовательности
"""

# creating
list1 = []  # empty
list2 = [1, 1, 2, 3, 7]
list3 = ['a', 'b', 'c']
list4 = [1, 'n', [8, 'e', '7'], '3', 0, 1.6]
list5 = list("string")

# operators
print("operator + (concatenate): ", list2 + list3)
print("operator * (repeat):", list5 * 2)
print("operator in : ", (0 in list4, 5 in list4))
list3[-1] = 1
print("operator = and index: ", list3)
print("operator == : ", list2 == list3)
print("index: ", (list4[2], list4[-4]))
print("slice: ", list4[1:4])
print("slice: ", list4[::2])
print("slice: ", list4[2][2])
print("-------------")

# built-in functions
print("length: ", len(list5))
print("list: ", list2, "type: ", type(list2))
print("list() function: ", list("dog"))
print("max = ", max(list2))
print("min = ", min(list2))
print("-------------")

# methods
list2.append("new element")  # append
print("append() method: ", list2)

list4.extend(list2)  # extend
print("extend() method: ", list4)

list4.insert(2, 'insert')  # insert
print("insert method: ", list4)

list2.remove(1)  # remove
print("remove method: ", list2)

print("pop method: ", list4.pop(2))  # pop

print("index method: ", list4.index(2, 0, len(list4)))  # index

print("count method: ", list4.count(1))  # count

list5.sort()  # sort
print("sort method: ", list5)

list5.reverse()  # reverse
print("reverse method: ", list5)

print("copy method: ", list4.copy())  # copy

list3.clear()  # clear
print("clear method: ", list3)

my_str = "It is a string"
my_list = my_str.split()
print(my_list)
print("-------------")

# list generator
print("list generators:")
list_gen = [i * 2 for i in "list"]
print(list_gen)
list_gen = [i + j for i in "list" for j in "cat"]
print(list_gen)
list_gen = [i ** 2 for i in range(1, 11)]
print(list_gen)
print("-------------")

# removal element(s)
print(list2)
del list2[2]
print(list2)
del list2[2:]
print(list2)
list2[0:1] = []
print(list2)
