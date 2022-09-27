#this is a guessing game

import random
n = random.randint(1, 100)

age = (input("Guess my age: "))

if age.isdigit():
    if int(age) > n:
        print("wow! I'm not that old")
    elif int(age) < n:
        print("Geez! I'm way older than that")
    else:
        print("You guessed it right")
        
else:
    print("WTF are you doing?")
