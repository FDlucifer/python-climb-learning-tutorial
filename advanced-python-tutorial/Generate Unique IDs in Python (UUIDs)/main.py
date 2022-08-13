import uuid
import pandas as pd

data = pd.DataFrame({
    "id": [uuid.uuid4() for _ in range(6)],
    "value": [40,20,10,20,30,30],
    "value2": [1,1,1,0,0,1]
})

data = data.set_index("id")
print(data)

existing = pd.read_csv("existing_data.csv")
existing = existing.set_index("id")

combined = pd.concat([existing, data], verify_integrity=True)
print(combined)

