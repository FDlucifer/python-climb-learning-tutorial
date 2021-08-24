from dataclasses import dataclass

@dataclass
class Investor:
    name: str
    age: int
    cash: float
    favoriteSport: str
    def __repr__(self):
        return "hello"

i1 = Investor("John", 80, 700, "Soccer")
i2 = Investor("Mike", 18, 2000, "Baseball")
i3 = Investor("John", 80, 700, "Basketball")

print(i1)
print(i1 == i2)
print(i1 == i3)