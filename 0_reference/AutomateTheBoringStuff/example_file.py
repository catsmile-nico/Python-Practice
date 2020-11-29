import os
path1 = "\\".join(["folder1","folder2","folder3","file.png"])
path2 = os.path.join("folder1","folder2","folder3","file.png")

print(path1)
print(path2)

# value join function uses
print(os.sep)

# current dir
currentDir = os.getcwd()
print(os.getcwd())

# change working dir
os.chdir("c:\\")
print(os.getcwd())

os.chdir(currentDir)
print(os.getcwd())

# absolute path
print(os.path.abspath("hello.bat"))

# check absolute path
print(os.path.isabs("..\\..\\hello.bat"))
print(os.path.isabs("c:\\folder\\folder"))

# relative path
print(os.path.relpath("c:\\folder1\\folder2\\spam.png","c:\\folder1"))

# directory path only
print(os.path.dirname("c:\\folder1\\folder2\\spam.png"))

# basename only
print(os.path.basename("c:\\folder1\\folder2\\spam.png"))

# check exist file
print(os.path.exists("c:\\folder1\\folder2\\spam.png"))

# check exist dir
print(os.path.exists("c:\\windows\\system32\\"))

# get size
print(os.path.getsize("c:\\windows\\system32\\"))
print(os.path.getsize("c:\\windows\\system32\\calc.exe"))

# list dir
print(os.listdir(os.getcwd()))

# total size
totalSize = 0
for filename in os.listdir(os.getcwd()):
    if not os.path.isfile(os.path.join(os.getcwd(), filename)):
        continue
    totalSize = totalSize + os.path.getsize(os.path.join(os.getcwd(), filename))

print(totalSize)

# create dir
os.makedirs(str((os.getcwd()) + "\\newfolder"))
