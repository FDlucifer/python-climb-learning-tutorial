import cbpro

public_client = cbpro.PublicClient()

eth_trades = public_client.get_product_trades('ETH-USD')
print(next(eth_trades))
print(next(eth_trades))
print(next(eth_trades))
print(next(eth_trades))
print(next(eth_trades))
print(next(eth_trades))