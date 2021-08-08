from difflib import SequenceMatcher

with open("1.txt") as file1, open("2.txt") as file2:
    file1data = file1.read()
    file2data = file2.read()
    similarity = SequenceMatcher(None, file1data, file2data).ratio()
    print(similarity * 100)