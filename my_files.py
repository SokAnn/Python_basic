"""
файлы: основы
"""

# open file
f = open("file.txt", "r")
# "r" - read file (default value)
# "w" - write file (content delete; file does not exist - create file)
# "x" - write file (file does not exist - exception)
# "a" - write file (add to end of file)
# "b" - open file (binary)
# "t" - open file (text)
# "+" - open file (read & write)

# read file
print(f.read())
# close file
f.close()

# examples
# 1
f = open("file.txt", "w")
print(f.write("New line...\n"))
f.close()
# 2
f = open("file1.txt", "x")
f.write("file 1...\n")
f.close()
# 3
f = open("file.txt", "a")
f.write("1234\n")
f.close()
# 4
f = open("file1.txt", "br")
print(f.read())
f.close()
# 5
f = open("file.txt", "a+")
print(f.read())
print(f.write("new stroka\n"))
f.close()

# with ... as ... - the best way to open a file (file will close by default)

# write()
with open("file2.txt", "w+") as f:
    f.write("file2\n")  # write one line
    print(100500, file=f)  # write data to file via print() function

# readline()
with open("file2.txt", "r") as f:
    print(f.readline())  # read one line

# readlines()
with open("file.txt", "r") as f:
    print(f.readlines())  # read lines
with open("file.txt", "r") as f:
    for line in f.readlines():
        print(line)

# writelines()
with open("file2.txt", "a") as f:
    f.writelines(["new line\n", "\n"])  # write lines

# fileno() & read(n) & tell() & seek() & seekable() & truncate() & flush()
f = open("file.txt", "r+")
print("info: ", f)  # print info about file
print("file data:\n", *f)  # print file data
print("file descriptor", f.fileno())  # file descriptor
print("temp position: ", f.tell())  # temp position
print(f.read(10))  # read n symbols or bytes
print("temp position: ", f.tell())
print(f.read(5))
print("temp position: ", f.tell())
print("new position: ", f.seek(0))  # new position
print("temp position: ", f.tell())
print("random access: ", f.seekable())  # checks file supports random access
f.truncate(5)  # reduces file size to n or temp position
print("file data:\n", *f)
print("terminal: ", f.isatty())  # returns True if the file is bound to the terminal
# print(f.buffer)
f.flush()  # clears the internal buffer
f.close()
