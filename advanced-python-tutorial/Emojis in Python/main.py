# pip install emoji beautifulsoup4

from emoji import emojize
from emoji_soup import get_emoji_data
from time import sleep

print('T-Rex', emojize(':T-Rex:'))
print(type(emojize(':T-Rex:')))

all_emojis = get_emoji_data()

for emoji in all_emojis:
    print(emojize(emoji), end='')