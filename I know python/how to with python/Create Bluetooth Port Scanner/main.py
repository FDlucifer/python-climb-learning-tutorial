# pip install pybluez

import bluetooth

print("looking for bluetooth devices ......... ")
devices = bluetooth.discover_devices(lookup_names=True)

for addr, name in devices:
    print("address : ", addr)
    print("name : ", name)