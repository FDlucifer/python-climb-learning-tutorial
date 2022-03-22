import time
import requests
import urllib.parse
import hashlib
import hmac
import base64

with open("keys", "r") as f:
    lines = f.read().splitlines()
    api_key = lines[0]
    api_sec = lines[1]

api_url = "https://api.kraken.com"

def get_kraken_signature(urlpath, data, secret):
    postdata = urllib.parse.urlencode(data)
    encoded = (str(data['nonce']) + postdata).encode()
    message = urlpath.encode() + hashlib.sha256(encoded).digest()

    mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)
    sigdigest = base64.b64encode(mac.digest())
    return sigdigest.decode()

def kraken_request(url_path, data, api_key, api_sec):
    headers = {"API-Key": api_key, "API-Sign": get_kraken_signature(url_path, data, api_sec)}
    resp = requests.post((api_url + url_path), headers=headers, data=data)
    return resp

resp = kraken_request("/0/private/AddOrder", {
    "nonce": str(int(1000 * time.time())),
    "ordertype": "limit"
    "type": "buy",
    "volume": 1.25,
    "pair": "XBTUSD",
    "price": 27500
}, api_key, api_sec)

print(resp.json())

buy_limit = 38000
sell_limit = 39000
buy_amount = 0.01
sell_amount = 0.01

while True:
    current_price = requests.get("http://api.kraken.com/0/public/Ticker?pair=BTCUSD").json()['result']['XXBTZUSD']['c'][0]
    print(current_price)
    if float(current_price) < buy_limit:
        print(f"Buying {buy_amount} of BTC at {current_price}!")

        resp = kraken_request("/0/private/AddOrder", {
            "nonce": str(int(1000 * time.time())),
            "ordertype": "market"
            "type": "buy",
            "volume": buy_amount,
            "pair": "XBTUSD",
        }, api_key, api_sec)

        if not resp.json()['error']:
            print("successfully bought BTC!")
        else:
            print(f"Error: {resp.json()['error']}")

    else:
        print(f"current price: {current_price}, not buying or selling")