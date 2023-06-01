from collections import defaultdict

my_dict = defaultdict(int)

print(my_dict['age'])

my_dict['some_other_value'] += 20
print(my_dict)

mylist = [1,2,3,4,5,6,7,8,9,10]
counter = defaultdict(int)
for element in mylist:
    counter[str(element)] += 1

print(counter)

tuple_list = [("a", 10), ("b", 4), ("a", 5), ("c", 7), ("b", 1)]
group_data = defaultdict(list)
for key, value in tuple_list:
    group_data[key].append(value)
print(group_data)
group_data = {k: sum(v) for k, v in group_data.items()}
print(group_data)

class MyDefaultDict(defaultdict):
    def __missing__(self, key):
        self[key] = value = len(key)
        return value

test = MyDefaultDict()
print(test["fdvoid0"])
print(test["luci11"])
print(test)

constant_default_dict = defaultdict(lambda: "hello world")
print(constant_default_dict["hello"])
