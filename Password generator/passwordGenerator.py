import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("PASSWORD GENERATOR PROJECT")

n_letters = int(input("How many letters would you like in your password: "))
n_numbers = int(input("How many numbers would you like in your password: "))
n_symbols = int(input("How many characters would you like in your password: "))

password_string = ""
for i in range(n_letters):
    letter_random = random.choice(letters)
    # print(letter_random)
    password_string += letter_random
# print(password_string)

for i in range(n_numbers):
    number_random = random.choice(numbers)
    # print(number_random)
    password_string += number_random
# print(password_string)

for i in range(n_symbols):
    symbols_random = random.choice(symbols)
    # print(symbols_random)
    password_string += symbols_random
# print(password_string)

print('\n')
print(f"Shhhh.. don't tell anyone your password is {password_string}")
