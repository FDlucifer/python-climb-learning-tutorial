import whois

sites = ["facebook.com", "twitter.com", "baidu.com", "meta.com", "whatsapp.com"]

companies = [whois.whois(s).org for s in sites]
print(companies)

creation_dates = [whois.whois(s).creation_date for s in sites]
print(creation_dates)

emails = [whois.whois(s).emails for s in sites]
print(emails)

print(sites[creation_dates.index(min(creation_dates))])


