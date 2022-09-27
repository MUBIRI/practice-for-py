#this is anguessing game
age = 16

try:
    age = input("Enter your age to continue.")
    print(age)
except:
    print("something went wrong,Please try again.")

age = int(age)
print(age)
if age > 16:
    print("congs you qualify to play this game.")
elif age == 16:
    print("wow!! welcome to the guessing game.")
else:
    print("We are sorry, you aint ligible to play this game")