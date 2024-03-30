message = "hello world! this is my message!"
binary = " ".join(format(ord(c), "b") for c in message)

print(binary)

binary_text = "1101000 1100101 1101100 1101100 1101111 100000 1110111 1101111 1110010 1101100 1100100 100001 100000 1110100 1101000 1101001 1110011 100000 1101001 1110011 100000 1101101 1111001 100000 1101101 1100101 1110011 1110011 1100001 1100111 1100101 100001"

normal = "".join(chr(int(c, 2)) for c in binary_text.split(" "))
print(normal)