from operator import length_hint
import string
from tokenize import Special

password = input("Enter the password: ")
# password = "casdcascasdncajkd7&**&&***dASD234]"

upper_case = any([1 if c in string.ascii_uppercase else 0 for c in password])
lower_case = any([1 if c in string.ascii_lowercase else 0 for c in password])
special = any([1 if c in string.punctuation else 0 for c in password])
digits = any([1 if c in string.digits else 0 for c in password])

characters = [upper_case, lower_case, special, digits]

length = len(password)

score = 0

with open('common.txt', 'r') as f:
    common = f.read().splitlines()

if password in common:
    print("Password was found in a common list, Score: 0 / 7")
    exit()

if length > 8:
    score += 1
if length > 12:
    score += 1
if length > 17:
    score += 1
if length > 20:
    score += 1

print(f"Password length is {str(length)}, adding {str(score)} points!")

if sum(characters) > 1:
    score += 1
if sum(characters) > 2:
    score += 1
if sum(characters) > 3:
    score += 1

print(f"password has {str(sum(characters))} different character types, adding {str(sum(characters) - 1)} points!")


if score < 4:
    print(f"the password is quite weak! score: {str(score)} / 7")
elif score == 4:
    print(f"the password is ok! score: {str(score)} / 7")
elif 4 < score < 6:
    print(f"the password is pretty good! score: {str(score)} / 7")
elif score > 6:
    print(f"the password is strong! score: {str(score)} / 7")
