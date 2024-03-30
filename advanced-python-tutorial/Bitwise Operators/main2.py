LUCI_READ = 0b1000
LUCI_WRITE = 0b0100
LUCI_EXEC = 0b0010
LUCI_CHANGE = 0b0001

def myfunction(permission):
    print(bin(permission))

myfunction(LUCI_WRITE | LUCI_READ)