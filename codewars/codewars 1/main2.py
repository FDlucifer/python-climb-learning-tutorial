# Disemvowel Trolls

def disemvowel(string_):
    vowels = "aeiou"
    for v in vowels:
        string_ = string_.replace(v, "")
        string_ = string_.replace(v.upper(), "")
    return string_