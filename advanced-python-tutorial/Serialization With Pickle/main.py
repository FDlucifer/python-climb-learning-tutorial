mytext = "Hello World"
myint = 18
myfloat = 7.657

with open('mydata.txt', 'w') as f:
    f.write(mytext + '\n')
    f.write(str(myint) + '\n')
    f.write(str(myfloat) + '\n')