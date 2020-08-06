#range with end only
for i in range(10):
    print(i)

#range with start and end
print (range(0,4))

#for loop also works with list
for i in [0,1,2,3]:
    print(i)

#printing range values as a list
print (list(range(0,4)))
print (list(range(0,100,2)))

#printing list values using len
supplies = ["pens", "staplers", "sword", "knife"]
for i in range(len(supplies)):
    print("Index " + str(i) + " is " + supplies[i])

#multiple assignment with 1 line part 1
cat = ["fat", "orange", "loud"]
size, color, disposition = cat
print (size)
print (color)
print (disposition)

#multiple assignment with 1 line part 2
size, color, disposition = "skinny", "black", "quiet"
print (size)
print (color)
print (disposition)

#multiple assignment with 1 line part 2
a = "AAA"
b = "BBB"
print (a, b)
a, b = b, a
print (a, b)
