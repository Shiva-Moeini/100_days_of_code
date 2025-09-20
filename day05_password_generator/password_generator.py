import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 'A','B','C','D','E','F','G','H','I','J','K','L','M',
   'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ["!", "#", "$", "%", "&", "*", "+"]

password = []

print("Welcome to the PyPassword Generator!")
number_of_letters = int(input("How many letters would you like in your password?\n"))
number_of_numbers = int(input("How many numbers would you like in your password?\n"))
number_of_symbols = int(input("How many symbols would you like in your password?\n"))

for _ in range (0, number_of_letters):
    password.append(random.choice(letters))

for _ in range (0, number_of_numbers):
    password.append(random.choice(numbers))

for _ in range (0, number_of_symbols):
    password.append(random.choice(symbols))

random.shuffle(password)

password_string = ""
for _ in password:
    password_string += _
print(password_string)
