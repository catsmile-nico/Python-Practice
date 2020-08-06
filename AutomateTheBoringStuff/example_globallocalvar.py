def spam():
    eggs = 99
    bacon()
    print(eggs) #does not use eggs in bacon cause its a var local to bacon

def bacon():
    ham = 101
    eggs = 0 

spam()


def spam2():
    print(eggs)

eggs = 42
spam2() #python will check if got global var


def spam3():
    eggs2 = "hello"
    print(eggs2)

eggs2 = 56
spam3() #python will check local var first
print(eggs2) #python only recognise global eggs2 here
