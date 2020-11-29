import shelve
shelfFile = shelve.open("data")
shelfFile["cats"] = ["bat", "rat" ,"lad"]
shelfFile.close()


shelfFile = shelve.open("data")
print(shelfFile["cats"])
print(list(shelfFile.keys()))
print(list(shelfFile.values()))
shelfFile.close()

