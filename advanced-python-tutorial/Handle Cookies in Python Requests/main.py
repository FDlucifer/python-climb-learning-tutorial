# https://www.stealmylogin.com/demo.html

import requests

s = requests.session()

login_url = "http://127.0.0.1:5000/login"
login_data = {"username": "testuser", "password": "testpass"}

res = s.post(login_url, json=login_data)

saved_cookies = res.cookies
print(saved_cookies)

if res.json().get("success"):
    print("login successful!")
else:
    print("login failed!")

protected_url = "http://127.0.0.1:5000/protected"

res = s.get(protected_url)

if res.json().get("access"):
    print("access granted!")
else:
    print("access denied!")
