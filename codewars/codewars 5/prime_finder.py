def is_prime(n):
    for number in range(2, n//2 + 1):
        if n % number == 0:
            return False
    return True

print([n for n in range(10, 100) if is_prime(n)])
# [11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
