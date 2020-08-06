from random import *

print ("Hello, whats your name?")
name = input()

num = randint(1,20)
print ("Hi " + name + ", I'm thinking of a number between 1 and 20")
print ("Take a guess, you have 6 tries") 

for guessTaken in range(6):
    guess = int(input())
    if guess < num:
        print("Your guess is too low")
    elif guess > num:
        print("Your guess is too high")
    else:
        break

if guess == num:
    print ("Good job " + name + ", you guessed it its " + str(num))
else:
    print ("Nope. The number is " + str(num))
