# pip install jsonschema

import json
from jsonschema import validate
from jsonschema import ValidationError

with open('person.json') as f:
    document = json.load(f)

with open('person-schema.json') as f:
    schema = json.load(f)

try:
    validate(instance=document, schema=schema)
    print("validation succeeded!")
except ValidationError as e:
    print("validation failed!")
    print(f"error message: {e.message}")
