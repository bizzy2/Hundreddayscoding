# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the PyPassword Generator!')

chooseletter = int(input('How many letters would you like in your password?'))

choosesym = int(input('How many symbols would you like?'))

choosenumb = int(input('How many numbers would you like?'))

# Easy level
import random

# password = ''
# for char in range(1, chooseletter + 1):
#    password += random.choice(letters)

# for char in range(1, choosesym + 1):
# password += random.choice(symbols)

# for char in range(1, choosenumb + 1):
# password += random.choice(numbers)

# print(password)

# Hard level

password = []

for char in range(1, chooseletter + 1):
    password += random.choice(letters)

for char in range(1, choosesym + 1):
    password += random.choice(symbols)

for char in range(1, choosenumb + 1):
    password += random.choice(numbers)

pass_output = ''

for i in password:
    pass_output += i

print(f'Your password is: {pass_output}')
