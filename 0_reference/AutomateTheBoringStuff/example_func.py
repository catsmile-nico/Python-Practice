def hello():
    print("Howdy")
    print("Howdy!!")
    print("Hello")

hello()
hello()
hello()

def hello2(name):
    print("Hello " + name)

hello2("test")

print("Hello has " + str(len("hello")) + " letters in it")

def plusOne(num):
    return num + 1

newNum = plusOne(5)
print(newNum)
