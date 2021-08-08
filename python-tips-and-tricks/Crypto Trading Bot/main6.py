from typing import Sized
import cbpro

data = open('passphrase', 'r').read().splitlines()

public = data[0]
passphrase = data[1]
secret = data[2]

auth_client = cbpro.AuthenticatedClient(public, secret, passphrase)

print(auth_client.buy(price="10.0", size="2.1", order_type="limit", product_id="ETH-EUR"))
print(auth_client.buy(price="10", order_type="market", product_id="ETH-EUR"))

print(auth_client.sell(price="2000000.00", size="10", order_type="limit", product_id="BTC-EUR"))
print(auth_client.sell(size="10", order_type="market", product_id="BTC-EUR"))

print(auth_client.place_limit_order(product_id="BTC-EUR", side="buy", price="10.00", size="2"))
print(auth_client.cancel_all(product_id="BTC-EUR"))

import time

sell_price = 28700
sell_amount = 0.3

buy_price = 28690
buy_amount = 0.2

while True:
    price = float(auth_client.get_product_ticker(product_id="BTC-EUR")['price'])
    if price <= buy_price:
        print(f"Buying BTC-EUR because price of {price:,} fell below buying price limit of {buy_price}")
        auth_client.buy(size=buy_amount, order_type="market", product_id="BTC-EUR")
    elif price >= sell_price:
        print(f"Selling BTC-EUR because price of {price:,} rose above selling price limit of {sell_price}")
        auth_client.sell(size=sell_amount, order_type="market", product_id="BTC-EUR")
    else:
        print(f"Not doing anything! Price is {price:,}!")
    time.sleep(2)