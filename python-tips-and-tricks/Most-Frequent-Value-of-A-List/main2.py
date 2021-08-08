mylist = [1,2,3,4,1,2,1,1,2,3,2,2,4,2,3,2,1,2,2,2,1,1,3,4]

print(set(mylist))
print(max(set(mylist), key=mylist.count))

most_frequent = max(set(mylist), key=mylist.count)
frequency = mylist.count(most_frequent)

print(most_frequent, frequency)