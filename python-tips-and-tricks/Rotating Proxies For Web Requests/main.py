import requests

with open("valid_proxies.txt", "r") as f:
    proxies = f.read().split("\n")

sites_to_check = ["http://cip.cc", "https://www.baidu.com", "https://www.google.com"]

counter = 0

for site in sites_to_check:
    try:
        print(f"using the proxy: {proxies[counter]}")
        res = requests.get(site, proxies={"http:": proxies[counter], "https:": proxies[counter]})
        print(res.status_code)
    except:
        print("failed")
    finally:
        counter += 1
        counter % len(proxies)

