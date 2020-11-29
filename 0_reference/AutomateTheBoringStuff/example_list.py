print("SPAM")
spam = ["cat","bat","dog","rat"]
print (spam)
print (spam[0])
print ("print counting backwards: " + spam[-1])
print ("print up till 3 but not 3: " + str(spam[1:3])) 
print ("print up till 2 but not 2: " + str(spam[:2]))
print ("print from 1 onwards: " + str(spam[1:])) 
print ("Length of spam is " + str(len(spam)))
print ([1,2,3] + [4,5,6])
print ([1,2,3] * 3)
print (list("HELLO"))
print ("howdy" in ["hello", "howdy", "hi"])

print("\nSPAM2")
spam2 = [["cat","bat","dog","rat"], ["10","20","30","40"]]
print (spam2[0][2])
print (spam2[1][2])


print("\nSPAM3")
spam3 = ["10","20","30","40"]
print (spam3)
spam3[2] = "Hello"
print (spam3)
spam3[1:2] = ["cat","bat","dog"] #insert between value 1 
print (spam3)
spam3 = ["10","20","30","40"]
print (spam3)
spam3[1:3] = ["cat","bat","dog"] #insert between values 1 and 2
print (spam3)
