with open('mydata.txt', 'r') as f:
    data = f.read().splitlines()
    mytext = data[0]
    myint = int(data[1])
    myfloat = float(data[2])

print(mytext)
print(myint)
print(myfloat)