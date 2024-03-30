is_hotspot = [False, False, False, False, False, False, True, False, False]

print(any(is_hotspot))

is_hotspot = {False, False, False, False, False, False, True, False, False}

print(is_hotspot)
print(any(is_hotspot))

is_hotspot = (False, False, False, False, False, False, True, False, False)
print(any(is_hotspot))

bowl = ["apple", "apple", "banana"]
shelf = ["chocolate", "cookies"]
bag = [bowl, shelf]
print(bag)

bag.extend(bowl)
print(bag)
bag.extend(shelf)
print(bag)

bag = [*bowl, *shelf]
print(bag)