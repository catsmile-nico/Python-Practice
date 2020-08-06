spam = ["hello","howdy","hi","hey"]
print(str(spam.index("hi"))) #use index method

spam.append("mouse") 
print(spam)

spam.insert(1,"chicken") #insert at pos 1
print(spam)

spam.remove("hi")
print(spam)

del spam[0]
print(spam)

spam2 = ["cat","bat","rat","cat","cat"]
spam2.remove("cat") #only first instance of cat will be removed
print(spam2)

spam3 = [10,73,2,1,25,-1]
print(spam3)
spam3.sort()
print(spam3)


spam4 = ["10","73","2","1","25","-1"] #string sorts alphabetically
print(spam4)
spam4.sort()
print(spam4)
spam4.sort(reverse=True) #sort reverse
print(spam4)
