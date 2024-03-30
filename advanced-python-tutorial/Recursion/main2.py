def fibonacci(n):
    a, b = 0, 1
    for _ in range(0, n):
        a, b = b, a + b
    return a

print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
print(fibonacci(100))

def fibonacci_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_recursive(20))