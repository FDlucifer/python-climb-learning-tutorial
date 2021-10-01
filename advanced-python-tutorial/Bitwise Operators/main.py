n1 = 23477
n2 = 31213

print(bin(n1)[2:])
print(bin(n2)[2:])

# and
n3 = n1 & n2
print(bin(n3)[2:])

# or
n4 = n1 | n2
print("0" + bin(n4)[2:])

# xor
n5 = n1 ^ n2
print(bin(n5)[2:])

# not
print(bin(~n1)[3:])
print("0" + bin(0b111111111111111 - n1)[2:])

# shifts
number = 20
print(bin(number))
number <<= 1
print(bin(number))
number >>= 2
print(bin(number))