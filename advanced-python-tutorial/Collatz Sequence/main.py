from functools import lru_cache


def collatz_sequence_iterative(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


print(collatz_sequence_iterative(5))


def collatz_length_iterative(n):
    counter = 1
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        counter += 1
    return counter


print(collatz_length_iterative(3003))


@lru_cache(maxsize=None)
def collatz_length_recursive(n):
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            return 1 + collatz_length_recursive(n // 2)
        else:
            return 1 + collatz_length_recursive(3 * n + 1)


longest = 0
longest_i = 1

for i in range(1, 1000000):
    length = collatz_length_recursive(i)
    if length > longest:
        longest = length
        longest_i = i

print(longest_i)
print(longest)
