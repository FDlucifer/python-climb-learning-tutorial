import time

host_path = "C:\Windows\System32\drivers\etc\hosts"
redirected = "127.0.0.1"
website_list = {"facebook.com", "www.facebook.com"}
while True:
    with open(host_path, 'r') as file:
        content = file.readlines()
        file.seek(0)
        for line in content:
            if not any(website in line for website in website_list):
                file.write(line)
        file.truncate()
        print("well done...")
    time.sleep(5)