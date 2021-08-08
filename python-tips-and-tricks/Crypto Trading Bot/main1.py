import cbpro

public_client = cbpro.PublicClient()

result = public_client.get_currencies()

for row in result:
    print(row['id'])