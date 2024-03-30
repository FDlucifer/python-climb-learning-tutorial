import ctypes

a = ctypes.c_int(200)
print(a.value)
print(a)
print(type(a.value))

b = ctypes.c_long(300)
ptr = ctypes.pointer(b)
print(ptr)
print(ptr.contents)
print(ptr.contents.value)
print(ctypes.addressof(ptr.contents))
ptr.contents.value = 23845234
print(b)

ptr_address = ctypes.addressof(ptr.contents)
ptr_new = ctypes.cast(ptr_address, ctypes.POINTER(ctypes.c_long))
print(ptr_new.contents.value)

