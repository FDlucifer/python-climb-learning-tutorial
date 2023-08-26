import string
import math

alphabet = string.ascii_lowercase


def moving_shift(s, shift):
    is_uppercase = [c.isupper() for c in s]
    s = s.lower()
    result = "".join(
        [
            alphabet[(alphabet.index(c) + shift + i) % len(alphabet)]
            if c in alphabet
            else c
            for i, c in enumerate(s)
        ]
    )
    result = "".join(
        [c.upper() if is_uppercase[i] else c for i, c in enumerate(result)]
    )
    if len(result) % 5 == 0:
        part_length = int(len(result) / 5)
        return [result[i * part_length : (i + 1) * part_length] for i in range(5)]
    else:
        part_length = math.ceil(len(result) / 5)
        return [result[i * part_length : (i + 1) * part_length] for i in range(4)] + [
            result[4 * part_length :]
        ]


def demoving_shift(s, shift):
    s = "".join(s)
    is_uppercase = [c.isupper() for c in s]
    s = s.lower()
    result = "".join(
        [
            alphabet[(alphabet.index(c) - shift - i) % len(alphabet)]
            if c in alphabet
            else c
            for i, c in enumerate(s)
        ]
    )
    result = "".join(
        [c.upper() if is_uppercase[i] else c for i, c in enumerate(result)]
    )
    return result
