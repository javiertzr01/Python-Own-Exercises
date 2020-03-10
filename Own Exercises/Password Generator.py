import random
import numpy as np
import string

lowercase = np.array([])
uppercase = np.array([])
digits = np.array([])
punctuation = np.array([])
for x in range(len(string.ascii_lowercase)):
    lowercase = np.append(lowercase, string.ascii_lowercase[x])
    lowercase = lowercase.astype('object')

for x in range(len(string.ascii_uppercase)):
    uppercase = np.append(uppercase, string.ascii_uppercase[x])
    uppercase = uppercase.astype('object')

for x in range(len(string.digits)):
    digits = np.append(digits, string.digits[x])
    digits = digits.astype('object')

for x in range(len(string.punctuation)):
    punctuation = np.append(punctuation, string.punctuation[x])
    punctuation = punctuation.astype('object')

possible_units = np.array([lowercase, uppercase, digits, punctuation])

pw_length = int(input("Please enter how long you want your password to be: "))
letter_length = int(input("Please enter how many letters you want your password to have: "))
digits_length = int(input("Please enter how many numbers you want your password to have: "))
while (letter_length + digits_length) > pw_length:
    print("Sorry, the number of letters and numbers you want your password to have exceeds your intended password length. Please try again")
    pw_length = int(input("Please enter how long you want your password to be: "))
    letter_length = int(input("Please enter how many letters you want your password to have: "))
    digits_length = int(input("Please enter how many numbers you want your password to have: "))
pw = np.array([])
for x in range(letter_length):
    number = random.randint(0, 1)
    letter_case = possible_units[number]
    letter_value = letter_case[random.randint(0, len(letter_case) - 1)]
    pw = np.append(pw,letter_value)
for x in range(digits_length):
    digits_chosen = possible_units[2]
    digits_value = digits_chosen[random.randint(0, len(digits_chosen) - 1)]
    pw = np.append(pw, digits_value)
for x in range(pw_length - digits_length - letter_length):
    symbol = possible_units[3]
    symbol_value = symbol[random.randint(0, len(symbol) - 1)]
    pw = np.append(pw, symbol_value)
random.shuffle(pw)
# for x in range(pw_length):
#     number1 = random.randint(0, len(possible_units) - 1)
#     first = possible_units[number1]
#     value = first[random.randint(0, len(first) - 1)]
#     pw = np.append(pw, value)
result = ''
for element in pw:
    result += str(element)
print(result)