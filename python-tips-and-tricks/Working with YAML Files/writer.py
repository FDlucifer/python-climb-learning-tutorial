import yaml

data = {
    "name": "luci",
    "age": 25,
    "languages": ["Python", "C", "Java"],
    "address": {
        "city": "NYC",
        "ZIP": "1234",
        "country": "US"
    }
}

with open("somefile.yaml", "w") as f:
    yaml.dump(data, f, default_flow_style=False)

