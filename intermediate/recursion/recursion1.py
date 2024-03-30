def fibonnacci(n):
    a, b = 0, 1
    for x in range(n):
        a, b = b, a+b
    return a

print(fibonnacci(1000))

def fibonnacci2(n):
    if n <= 1:
        return n
    else:
        return (fibonnacci2(n-1) + fibonnacci2(n-2))

print(fibonnacci(1000))