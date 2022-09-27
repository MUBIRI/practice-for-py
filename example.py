print("hello ")

first_name = input("what is your first name?")
second_name = input("what is your last name?")
age = input("how old are you?")
print(first_name)
print(second_name)
print(age)
print(f"hello {first_name}, how are you doing today?")
age = int(age)
if age > 18:
    print("thank you{first_name}. you qualify for the adult policy")
elif age == 18:
    print("Congrates {first_name} you made it to the adult policy")
else:
    print("Sorry {first_name} you dont qualify for the adult policy")
