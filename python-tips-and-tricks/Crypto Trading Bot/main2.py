import cbpro

public_client = cbpro.PublicClient()

result = public_client.get_time()

print(result)