import os

# read as a string
helloFile = open(str((os.getcwd()) + "\\hello.py"))
print(helloFile.read())
helloFile.close()

# read as a list
helloFile = open(str((os.getcwd()) + "\\hello.py"))
print(helloFile.readlines())
helloFile.close()

# write to file
writeFile = open(str((os.getcwd()) + "\\hello.txt"), "w")
print(writeFile.write("hello!!!")) #return no. of char written
writeFile.close

writeFile = open(str((os.getcwd()) + "\\hello.txt"))
print(writeFile.read())
writeFile.close()

# append to file
writeFile = open(str((os.getcwd()) + "\\hello.txt"), "a")
writeFile.write("\nhello again?")
writeFile.close

writeFile = open(str((os.getcwd()) + "\\hello.txt"))
print(writeFile.read())
writeFile.close()
