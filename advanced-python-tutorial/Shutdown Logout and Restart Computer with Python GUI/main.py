from tkinter import *
import os

from pip import main

def shutdown():
    return os.system("shutdown /s /t 0")

def restart():
    return os.system("shutdown /r /t 0")

def logout():
    return os.system("shutdown -l")

master = Tk()

master.configure(bg='orange')
Button(master, text='shutdown', command=shutdown).grid(row=0)
Button(master, text='restart', command=restart).grid(row=1)
Button(master, text='log out', command=logout).grid(row=2)

mainloop()