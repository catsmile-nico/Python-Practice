mylist = list("hello")
print(mylist)

name = "test"
print(name[0])
print(name[1:3])

print("st" in name)
print("xx" in name)

for letter in name:
    print(letter)

# to create new string
name = "test is a cat"
newName = name[0:4] + " the " + name[10:13]
print(newName)


# using a function to append
def eggs(someParam):
    someParam.append("Hello")

spam = [1,2,3]
eggs(spam)
print("using a function to append" + str(spam))

# passing list var to another
spam = ["A", "B", "C", "D"]
cheese = spam
print(spam)
cheese[1] = 42
print("spam but edit cheese" + str(spam))
print("cheese" + str(spam))

# passing list var to create a new duplicate
import copy
spam = ["A", "B", "C", "D"]
cheese = copy.deepcopy(spam)
cheese[1] = 42

print(cheese)

print("wow" + \
        "wowow")
