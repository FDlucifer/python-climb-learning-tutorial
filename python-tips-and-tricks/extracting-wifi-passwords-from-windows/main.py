import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
wifis = [line.split(':')[1][1:-1] for line in data if "所有用户配置文件" in line]

for wifi in wifis:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', wifi, "key=clear"]).decode('utf-8').split('\n')
    results = [line.split(':')[1][1:-1] for line in results if "关键内容" in line]
    try:
        print(f"name: {wifi}, password: {results[0]}")
    except IndexError:
        print(f"name: {wifi}, password: cannot be read!")