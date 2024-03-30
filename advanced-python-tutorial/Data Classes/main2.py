from dataclasses import dataclass, field

@dataclass(order=True)
class Investor:
    sort_index: float = field(init=False, repr=False)
    name: str
    age: int
    cash: float = field(repr=True)

    def __post_init__(self):
        self.sort_index = self.cash

i1 = Investor("John", 80, 2000)
i2 = Investor("Mike", 18, 2000)
i3 = Investor("Anna", 50, 1000)
i2 = Investor("Bob", 70, 800000)
i3 = Investor("Charles", 18, 3000)

print(i1)
print(i1 < i2)
print(i1 > i3)
print(i1 == i3)