print("how many cats you have?")
numCats = input()
try:
    if int(numCats) >= 4:
        print("thats alot cats")
    else:
        print("so little cats")
except ValueError:
    print("you didnt enter number")
