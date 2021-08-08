# pip install cbpro

import cbpro

public_client = cbpro.PublicClient()

result = public_client.get_products()

for row in result:
    print(row['id'])