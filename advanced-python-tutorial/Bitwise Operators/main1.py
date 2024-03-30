person1 = 0b1000
person2 = 0b1110
person3 = 0b1111
person4 = 0b1010
person5 = 0b1101

together1 = person1 & person2 & person3 & person4 & person5
together2 = person1 | person2 | person3 | person4 | person5

print(bin(together1))
print(bin(together2))