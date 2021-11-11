"""
множества: основы
изменяемые, неиндексируемые, элементы хешируемые (неизменяемые) и уникальные (нет дубликатов)
произвольный порядок
"""

# creating
set1 = {1, 2, 3, 4}
set2 = {"cat", "dog", "mouse"}
set3 = {(1, 2, 3), (4,), (5, 6)}
set4 = {1, 2, "tree", (7, 9)}
set5 = set([0, 0, 5, 7, 9])
set6 = set()  # empty
print(f"{set4}\t{set5}\t{set6}")
print("-------------")

# operators
print("operator in :", ("cat" in set2, "tree" in set2))
print("operator | :", set1 | set4)
print("operator & :", set1 & set4)
print("operator - :", set1 - set4)
print("operator ^ :", set1 ^ set4)
print("operator <= : ", set1 <= {1, 2, 3, 4, 5, 6, 7})
print("operator >= : ", {1, 2, 3, 4, 5, 6, 7} >= set1)
print("-------------")

# built-in functions
print("type() function: ", type(set1))
print("length: ", len(set1))
print("-------------")

# methods
set2.add("tree")  # add()
print("add() method: ", set2)

set2.discard("tree")  # discard()
print("discard() method: ", set2)

set2.remove("mouse")  # remove() - equal discard(), but returns error if element doesn't exist in set
print("remove() method: ", set2)

print("pop() method: ", set3.pop())  # pop()

set3.clear()  # clear()
print("clear() method: ", set3)

res = set1.union(set4)  # union() - equal operator |
print("union() method: ", res)

res = set1.intersection(set4)  # intersection() - equal operator &
print("intersection() method: ", res)

res = set1.difference(set4)  # difference() - equal operator -
print("difference() method: ", res)

res = set1.symmetric_difference(set4)  # symmetric_difference()
print("symmetric_difference() method: ", res)

res = set2.copy()  # copy()
print("copy() method: ", res)

res = set1.isdisjoint(set4)  # isdisjoint()
res1 = set1.isdisjoint({8, 7, 9})
print("isdisjoint() method: ", (res, res1))

res = set1.issubset({1, 2, 3, 4, 5, 6, 7})  # issubset()  - equal operator <=
print("issubset() method: ", res)

res = set1.issuperset({1, 2})  # issuperset() - equal operator >=
print("issuperset() method: ", res)
print("-------------")

# frozenset
# неизменяемые - immutable
print("frozenset & methods:")
x = frozenset([1, 2, 3, 4, 5, 6])
y = frozenset([5, 6, 7, 8, 9])
print(x, type(x))
res = x.copy()  # copy()
print("copy() method: ", res)

res = x.isdisjoint({10, 11, 12})  # isdisjoint()
print("isdisjoint() method: ", res)

res = x.intersection(y)  # intersection()
print("intersection() method: ", res)

res = x.union(y)  # union()
print("union() method: ", res)

res = x.issuperset({5, 6})  # issuperset()
print("issuperset() method: ", res)

res = x.issubset({1, 2, 3, 4, 5, 6, 7, 8, 9})  # issubset()
print("issubset() method: ", res)

res = x.difference(y)  # difference()
print("difference() method: ", res)

res = x.symmetric_difference(y)  # symmetric_difference()
print("symmetric_difference() method: ", res)
