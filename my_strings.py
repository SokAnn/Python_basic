"""
строки: основы
неизменяемые, последовательности
"""

# creating - создание
stroka = "It is a string!"
S1 = 'str'
S2 = "str"
S3 = '''str'''
S4 = """str"""
S5 = "s\np\ta\nbbb\n"  # escape sequences
S6 = r"C:\Downloads"  # raw strings (no escapes)
B = b"sp\xc4m"  # byte strings
U = u"sp\u00c4m"  # Unicode strings
print("My string: ", stroka)
print(S1, S2, S3, S4, "\n", S5, S6, B, U)
print("-------------")

# operators (операторы): +, *, in, not in, [index], [start:stop:step], <, >, <=, >=, ==, !=
print("operator + (concatenate): ", stroka + " New stroka!")
print("operator * (repeate):", stroka * 3)
print("operator in :", ("is" in stroka, "no" in stroka))
print("operator not in :", ("is" not in stroka, "no" not in stroka))
print("index: ", stroka[0], stroka[1], stroka[8], stroka[-12])
print("-------------")
print("slice: ", stroka[:])
print("slice: ", stroka[0:7])
print("slice: ", stroka[::-1])
print("slice: ", stroka[::2])
print("-------------")
print("aa > Aa", "aa" > "Aa")
print("aa > 1a", "aa" > "Aa")
print("aa < Aa", "aa" < "Aa")
print("aa < 1a", "aa" < "Aa")
print("A < 1", "A" < "1")
print("A > 1", "A" > "1")
print("A >= 1", "A" >= "1")
print("A <= 1", "A" <= "1")
print("a == A", "a" == "A")
print("a != A", "a" != "A")
print("-------------")

# built-in functions (встроенные функции)
print("char by number - chr() function: ", chr(70))
print("number by char - ord() function: ", ord("a"))
print("length: ", len(stroka))
print("object to string - str() function: ", type(10), str(10), type(str(10)))
print("-------------")

# methods (методы)
print("substring find (first entry): ", (stroka.find("s"), stroka.find("s", 1, 5)))
print("substring find (last entry): ", (stroka.rfind("s"), stroka.rfind("s", 1, 5)))
print("getting the index: ", (stroka.index("s"), stroka.rindex("s")))
print("replacing part of a string: ", (stroka.replace("string", "cat"), stroka.replace(" ", "_", 2)))
print("splitting a string using a delimiter: ", stroka.split(" "))
print("splitting a string: ", "\nst\rr\nok\na".splitlines())
print("-------------")
print("string consists of digits: ", (stroka.isdigit(), "1340".isdigit()))
print("string consists of letters: ", (stroka.isalpha(), "dhyhwdgtt".isalpha()))
print("string consists of digits and letters: ", (stroka.isalnum(), "dcdc53hgf6".isalnum()))
print("string consists of lowercase letters: ", (stroka.islower(), "abcdef".islower()))
print("string consists of uppercase letters: ", (stroka.isupper(), "ABCD".isupper()))
print("string consists of non-displayed characters: ", (stroka.isspace(), " \n  \t".isspace()))
print("words in line begin with capital letter: ", (stroka.istitle(), "".istitle()))
print("-------------")
print("string to uppercase: ", stroka.upper())
print("string to lowercase: ", stroka.lower())
print("string starts with substring: ", (stroka.startswith("It"), stroka.startswith("kek")))
print("string ends with substring: ", (stroka.endswith("ing!"), stroka.endswith("kek")))
print("join() function: ", " ".join(["lol", "\t", "kek"]))
print("first letter of string to uppercase: ", (stroka.capitalize(), "abcd".capitalize()))
print("centering of string: ", stroka.center(len(stroka) + 4, "_"))
print("-------------")
print("counting number of entries of substring in string: ", stroka.count("str", 0, len(stroka)))
print("expandtabs() function: ", "\tst\t\troka\t".expandtabs(1))
print("removing spaces at the beginning of string: ", stroka.lstrip())
print("removing spaces at the end of string: ", stroka.rstrip())
print("partition() function: ", (stroka.partition("s"), stroka.rpartition("s")))
print("-------------")
print("swaps lowercase and uppercase: ", stroka.swapcase())
print("all words begin with uppercase letter: ", stroka.title())
print("zfill() function: ", stroka.zfill(20))
print("ljust() function: ", stroka.ljust(20, "_"))
print("rjust() function: ", stroka.rjust(20, "_"))
print("-------------")

# string formatting (форматирование строк)
print("\tString formatting:")
print("My string is \'%s\'" % stroka)  # operator %
print("%d %c" % (97, chr(97)))
print("My string is \'{}\'".format(stroka))  # method format()
print("{0}, {1}, {2}".format("one", "two", "three"))
print(f"My string is \'{stroka}\'")  # f-string (Python 3.6+)
