import json

with open('mydata.json', 'r') as f:
    json_object = json.loads(f.read())

print(json_object['people'][0]['name'])