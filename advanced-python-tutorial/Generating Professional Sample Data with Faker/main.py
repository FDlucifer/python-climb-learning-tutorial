# pip install faker

import random
from faker import Faker
from faker.providers import BaseProvider, DynamicProvider

f = Faker()

print(f.name())
print(f.address())
print(f.ipv4_private())
print(f.ipv4_public())
print(f.sentence())
print(f.zipcode())
print(f.locale())
print(f.license_plate())
print(f.phone_number())

for _ in range(10):
    print(f.unique.random_int(min=1, max=10))

for _ in range(5):
    print(f.bothify(text="????-########-??", letters="ABCDEFG"))
    print(f.hexify(text="MAC: ^^:^^:^^:^^:^^:^^", upper=True))

class NeuralProvider(BaseProvider):
    def video_categoty(self):
        return random.choice(["Machine Learning", "Vim", "Linux", "Finance"])

    def video_title(self):
        return "TITLE"

f.add_provider(NeuralProvider)
print(f.video_categoty())
print(f.video_title())

programming_language_provider = DynamicProvider(
    provider_name="programming_language",
    elements=["Python", "Go", "JS", "Ruby", "C#"]
)

f.add_provider(programming_language_provider)
print(f.programming_language())