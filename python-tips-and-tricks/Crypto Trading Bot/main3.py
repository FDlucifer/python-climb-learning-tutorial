import cbpro

public_client = cbpro.PublicClient()

result = public_client.get_product_order_book('BTC-USD')
print(result)

result1 = public_client.get_product_ticker('BTC-USD')
print(result1)

result2 = public_client.get_product_24hr_stats('BTC-USD')
print(result2)