def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception ("Symbol can only have 1 char")

    print(symbol * width)

    for i in range (height-2):
        print(symbol + (' ' * (width-2)) + symbol)

    print(symbol * width)

boxPrint("*", 15,5)
boxPrint("OO", 5,16)
