import traceback

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        try:
            raise Exception ("Symbol can only have 1 char")
        except:
            errorFile = open("error_log.txt","w")
            errorFile.write(traceback.format_exc())
            errorFile.close()
            print("The traceback info was written into error_log.txt")

    print(symbol * width)

    for i in range (height-2):
        print(symbol + (' ' * (width-2)) + symbol)

    print(symbol * width)

boxPrint("*", 15,5)
boxPrint("OO", 5,16)
