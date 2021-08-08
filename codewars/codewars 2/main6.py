# Where my anagrams at?

def anagrams(word, words):
    anagrams_list = []
    for w in words:
        if sorted(word) == sorted(w):
            anagrams_list.append(w)
    return anagrams_list