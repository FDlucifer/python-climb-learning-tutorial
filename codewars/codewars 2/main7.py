# Where my anagrams at?

def anagrams(word, words):
    return [w for w in words if sorted(w) == sorted(word)]