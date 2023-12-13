# pip install "python-benedict[all]"

from benedict import benedict

normal_dict = {"a": {"b": {"c": 10}}}

print(normal_dict["a"]["b"]["c"])

special_dict = benedict(normal_dict)

print(special_dict)
print(special_dict.a.b.c)

special_dict["x", "y", "z"] = 20

print(special_dict)

special_dict = benedict(keyattr_dynamic=True)
special_dict.a.b.c.d.e.f = 100

print(special_dict)
print(special_dict.to_xml())

test = benedict({'a': 10, 'b': 20, 'c': 30})

print(test.filter(lambda k, v: v > 25 or v < 15))

# print(benedict.from_csv("data.csv"))
# print(benedict.from_json("data.json"))
# print(benedict.from_xml("data.xml"))

data = {
    'people': [
        {'name': 'alice', 'country_code': 'US'},
        {'name': 'bob', 'country_code': 'US'},
        {'name': 'carlos', 'country_code': 'MX'},
        {'name': 'daniela', 'country_code': 'MX'},
        {'name': 'eric', 'country_code': 'DE'}
    ]
}

d = benedict(data)

print(d.groupby('people', by_key='country_code'))
