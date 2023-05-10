from math import gcd

def coins(coin1, coin2):
    return -1 if gcd(coin1, coin2) != 1 else (coin1 - 1) * (coin2 - 1) - 1
