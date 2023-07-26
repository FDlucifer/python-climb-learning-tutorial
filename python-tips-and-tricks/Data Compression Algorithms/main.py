import time
import lzma
import gzip
import bz2

data = b'this is some sample data' * 990000

print('original data size: ', len(data))

start = time.time()
compressed_data_lzma = lzma.compress(data)
end = time.time()

print(start - end)
print(len(compressed_data_lzma))

start = time.time()
compressed_data_gzip = gzip.compress(data)
end = time.time()

print(start - end)
print(len(compressed_data_gzip))

start = time.time()
compressed_data_bz2 = bz2.compress(data)
end = time.time()

print(start - end)
print(len(compressed_data_bz2))
