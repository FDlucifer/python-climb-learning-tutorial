import yaml

with open("complex.yml", "r") as f:
    data = yaml.safe_load(f)

print(data)

