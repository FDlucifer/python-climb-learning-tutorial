print(f"{0.1:.60f}")
print(f"{0.2:.60f}")
print(f"{0.1 + 0.2:.60f}")
print(f"{0.3:.60f}")

import struct

number = 0.1
binary_representation = struct.pack('>d', number)
binary_representation = "".join(f"{b:08b}" for b in binary_representation)
binary_representation = binary_representation[0] + " " + binary_representation[1:12] + " " + binary_representation[12:]
print(f"0.1 is {binary_representation}")

number1 = 0.2
binary_representation = struct.pack('>d', number1)
binary_representation = "".join(f"{b:08b}" for b in binary_representation)
binary_representation = binary_representation[0] + " " + binary_representation[1:12] + " " + binary_representation[12:]
print(f"0.2 is {binary_representation}")

number2 = 0.3
binary_representation = struct.pack('>d', number2)
binary_representation = "".join(f"{b:08b}" for b in binary_representation)
binary_representation = binary_representation[0] + " " + binary_representation[1:12] + " " + binary_representation[12:]
print(f"0.3 is {binary_representation}")

number3 = 0.1 + 0.2
binary_representation = struct.pack('>d', number3)
binary_representation = "".join(f"{b:08b}" for b in binary_representation)
binary_representation = binary_representation[0] + " " + binary_representation[1:12] + " " + binary_representation[12:]
print(f"sum is {binary_representation}")

from decimal import Decimal

print(round(Decimal('2.675'), 2))

one = Decimal('0.1')
two = Decimal('0.2')
three = Decimal('0.3')
result = one + two

print(one)
print(two)
print(three)
print(result)