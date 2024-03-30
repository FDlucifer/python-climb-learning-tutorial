# pip install thefuzz
# pip install fuzzywuzzy
# pip install python-Levenshtein
# pip install python-Levenshtein-wheels

from thefuzz import fuzz, process

s1 = "Just a test"
s2 = "just a test, cadcasdcasd"

print(fuzz.ratio(s1, s2))
print(fuzz.partial_ratio(s1, s2))
print(fuzz.token_sort_ratio(s1, s2))
print(fuzz.token_set_ratio(s1, s2))

things = ["Programming Language", "Native Language", "React Native", "Some Stuff", "Hello World", "Coding and Stuff"]

print(process.extract("language", things, limit=2))
print(process.extractOne("programming", things))