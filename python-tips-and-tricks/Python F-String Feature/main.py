name = 'Mike'

def hello():
    return 'hello'

print(f'hello {hello()}!')
print(f'here is a calculation 20 + 40 = {20 + 40}!')
print(f'here is a calculation {20 + 40 = }!')

def mysquare(n):
    return n ** 2

print(f"here is a function call: {mysquare(10) = }")

for i in range(10):
    value = i * mysquare(i)
    print(f'[DEBUG] {i = }, {mysquare(i) = }')
