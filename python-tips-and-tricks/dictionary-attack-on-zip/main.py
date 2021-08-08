import zipfile
import itertools

keywords = ['mike', 'smith', 'anna', '0802', '821995', '08021995', '95', '1995', 'ilove', 'barcelona']
combinations = itertools.combinations(keywords, 2)
# permutations = itertools.permutations(keywords, 2)

final_combinations = []

for combination in combinations:
    final_combinations.append(combination[0] + combination[1])

print(final_combinations)

'''
for permutation in permutations:
    print(permutation)
'''

z = zipfile.ZipFile('secret.zip')

wordlist = open('cain.txt', 'r').read()
wordlist = wordlist.splitlines()

wordlist.extend(final_combinations)

tries = 0

for word in wordlist:
    try:
        tries += 1
        z.setpassword(word.encode('ascii'))
        z.extract('secret.txt')
        print(f"successfully cracked after {tries} tries! passowrd was: {word}")
        break
    except:
        pass