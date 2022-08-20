# pip install getch

from getpass import getpass
import getch

def encoded_input(message):
    print(message, end="")
    pw = ""
    while True:
        symbol = getch.getch()
        if symbol == "\n" or symbol == "\r":
            break
        print("*", end="", flush=True)
        pw += symbol
    print()
    return pw

username = input("enter username: ")
password = encoded_input("enter password: ")

# send info to API
print(f"connecting with username {username} and password {password}")