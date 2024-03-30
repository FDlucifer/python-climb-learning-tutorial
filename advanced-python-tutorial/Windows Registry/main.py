import winreg

path = winreg.HKEY_CURRENT_USER

software = winreg.OpenKeyEx(path, r"SOFTWARE\\")
new_key = winreg.CreateKey(software, "lUc1f3r11")

winreg.SetValueEx(new_key, "myvalue", 0, winreg.REG_SZ, "hello world")
winreg.SetValueEx(new_key, "myothervalue", 0, winreg.REG_SZ, "20")

if new_key:
    winreg.CloseKey(new_key)

test = winreg.OpenKeyEx(path, r"SOFTWARE\\test\\")

myvalue = winreg.QueryValueEx(test, "myvalue")
myothervalue = winreg.QueryValueEx(test, "myothervalue")

if test:
    winreg.CloseKey(test)

print(myvalue[0])
print(myothervalue[0])

