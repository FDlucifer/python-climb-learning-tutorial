# Counting Duplicates

def duplicate_count(text):
    occurred = []
    found = []
    counter = 0
    for letter in text:
        if letter.lower() not in occurred:
            occurred.append(letter.lower())
        else:
            if letter.lower() not in found:
                counter += 1
                found.append(letter.lower())
    return counter