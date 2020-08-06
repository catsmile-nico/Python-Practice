message = "nice day to fish today"
count = {}

print("Working".rjust(20,"-"))
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1
print(count)

print("\n")
print("Error".rjust(20,"-"))
# if dont set default, error thay key doesnt exist
count2 = {}
for character in message:
    #count2.setdefault(character, 0)
    try:
        count2[character] = count2[character] + 1
    except KeyError:
        print("Key does not exist")
print(count2)
