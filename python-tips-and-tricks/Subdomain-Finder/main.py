import requests

domain = 'neuralnine.com'

file = open('subdomains.txt', 'r')

content = file.read()
subdomains = content.splitlines()

for subdomain in subdomains:
    url = f'http://{subdomain}.{domain}'
    try:
        requests.get(url)
    except requests.ConnectionError:
        pass
    else:
        print("Discovered Subdomain: ", url)