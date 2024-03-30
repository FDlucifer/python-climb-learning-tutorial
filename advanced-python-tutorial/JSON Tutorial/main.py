import json

mydict = {
    "people": [
        {
            "name": "bob",
            "age": 28,
            "weight": 80
        },
        {
            "name": "charles",
            "age": 45,
            "weight": 78
        },
        {
            "name": "danial",
            "age": 21,
            "weight": 110
        }
    ]
}

json_string = json.dumps(mydict, indent=2)
with open('mydata.json', 'w') as f:
    f.write(json_string)