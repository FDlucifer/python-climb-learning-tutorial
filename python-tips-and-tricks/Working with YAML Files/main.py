import yaml

with open("example.yml", "r") as f:
    data = yaml.safe_load(f)

print(data)

