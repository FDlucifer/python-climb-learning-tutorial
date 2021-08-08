values = [1,2,3,4,5,6,7,8]

revlist = []
for index in range(len(values)):
    revlist.append(values[len(values) - index - 1])
print(revlist)