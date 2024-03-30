import math

number = 1923347655123

print(len(str(number)))

if number > 0:
    print(int(math.log10(number)) + 1)
elif number < 0:
    print(int(math.log10(-number)) + 1)
else:
    print(1)