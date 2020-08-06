print("Using a key".rjust(20,"-"))
myCat = {"size":"fat", "color":"gray", "disposition":"loud"}
print(myCat["size"])

# list is ordered
print("\n")
print("List vs Dict".rjust(20,"-"))
print([1, 2, 3] == [3, 2, 1])

# dictionary unordered
eggs = {"name": "Zophie", "species":"cat", "age":8}
ham = {"species":"cat", "name": "Zophie", "age":8}
print(eggs == ham)

print("\n")
print("Check key exist".rjust(20,"-"))
# check key
print ("name" in eggs)

# list keys
print("\n")
print("List Keys".rjust(20,"-"))
print(eggs.keys())
print(list(eggs.keys()))
print(list(eggs.values()))
print(list(eggs.items()))

for k in eggs.keys():
    print(k)

# return something if key doesnt exist
print("\n")
print("Get key".rjust(20,"-"))
print(eggs.get("age",0))
print(eggs.get("agee",0))

# insert into dictionary
print("\n")
print("Insert".rjust(20,"-"))
print(list(eggs.items()))
if "color" not in eggs:
    eggs["color"] = "black"
print(list(eggs.items()))

# fixed dictionary keys
print("\n")
print("Set default key".rjust(20,"-"))
eggs = {"name": "Zophie", "species":"cat", "age":8}
eggs.setdefault("colors", "white")
print(list(eggs.items()))
eggs.setdefault("colors", "black")
print(list(eggs.items()))
eggs["colors"] = "black"
print(list(eggs.items()))
