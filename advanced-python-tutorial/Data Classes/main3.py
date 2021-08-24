from dataclasses import dataclass, field

@dataclass(order=True, unsafe_hash=True)
class Investor:
    sort_index: float = field(init=False, repr=False, hash=False)
    name: str
    age: int
    cash: float = field(repr=True, hash=False)

    def __post_init__(self):
        self.sort_index = self.cash

i1 = Investor("John", 80, 2000)
i2 = Investor("Mike", 18, 200)
i3 = Investor("Anna", 50, 1000)
i4 = Investor("Bob", 70, 800000)
i5 = Investor("Charles", 18, 3000)

mylist = [i1, i2, i3, i4, i5]
mylist.sort()
print(mylist)

print(hash(i1))
print(hash(i2))