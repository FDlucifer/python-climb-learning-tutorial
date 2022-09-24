import json

with open("response1.json", "r") as f:
    data = json.load(f)

print(data['receipts'][0].keys())


items = data['receipts'][0]['items']
print(items)

print(f"your purchase at {data['receipts'][0]['merchant_name']}")

for item in items:
    print(f"{item['description']} - {data['receipts'][0]['currency']}{item['amount']}")

print("-" * 30)
print(f"subtotal: {data['receipts'][0]['currency']} {data['receipts'][0]['subtotal']}")
print(f"tax: {data['receipts'][0]['currency']} {data['receipts'][0]['tax']}")
print("-" * 30)
print(f"total: {data['receipts'][0]['currency']} {data['receipts'][0]['total']}")

