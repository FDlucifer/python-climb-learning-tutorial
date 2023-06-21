# pip install requests

import random

random.seed(20)
random_number = random.randint(0, 10)

print(random_number)

import requests

url = "https://www.random.org/integers/?num=1&min=0&max=100&col=5&base=10&format=plain&rnd=new"
number = requests.get(url)
print(int(number.text))
