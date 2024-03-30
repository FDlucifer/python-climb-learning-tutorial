import whois

res = whois.whois("baidu.com")

print(res)
print(res.org)
print(res.creation_date)

