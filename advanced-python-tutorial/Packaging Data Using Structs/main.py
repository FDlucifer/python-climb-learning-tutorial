import struct

byte_stream = struct.pack("HHH", 10,20,30)
print(struct.calcsize("i"))
print(byte_stream)

a,b,c = struct.unpack("HHH", byte_stream)
print(a)
print(b)
print(c)

company = b"NeuralNine"
day, month, year = 1, 1, 2022
awesome = True

byte_stream = struct.pack("10s 3i ?", company, day, month, year, awesome)
print(byte_stream)
print(struct.unpack("10s 3i ?", byte_stream))

