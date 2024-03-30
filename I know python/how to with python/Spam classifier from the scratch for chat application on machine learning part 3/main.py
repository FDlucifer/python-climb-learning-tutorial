# pip install pandas
# pip install scipy

import socket
import time
import threading
from tkinter import *
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB

dataframe = pd.read_csv("spam.csv", encoding="latin-1")
dataframe.read()

dataframe.drop(['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4'], inplace=True, axis=1)
dataframe['v1'].replace({'ham':'1', 'spam':'0'}, inplace=True)
dataframe.drop_duplicates(inplace=True)

cv = CountVectorizer()

x = dataframe['v2']
y = dataframe['v1']

x = cv.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)
model = MultinomialNB()
model.fit(x_train, y_train)

root = Tk()
root.geometry("300x500")
root.config(bg="white")

def func():
    t = threading.Thread(target=recv)
    t.start()

def recv():
    global model
    listensocket = socket.socket()
    port = 3050
    maxconnection = 99
    ip = socket.gethostname()
    print(ip)

    listensocket.bind(('', port))
    listensocket.listen(maxconnection)
    (clientsocket, address) = listensocket.accept()

    while True:
        sendermessage = clientsocket.recv(1024).decode()
        if not sendermessage == "":
            sendermessages = [sendermessage]
            checkmsg = cv.transform(sendermessages)
            prediction = model.predict(checkmsg)
            print(prediction)
            time.sleep(5)
            lstbx.insert(0, "Client : " + sendermessage)

s = 0

def sendmsg():
    global s
    if s == 0:
        s = socket.socket()
        hostname = 'DESKTOP-9LSPC40'
        port = 4050
        s.connect((hostname, port))
        msg = messagebox.get()
        lstbx.insert(0, "You : " + msg)
        s.send(msg.encode())
    else:
        msg = messagebox.get()
        lstbx.insert(0, "You : " + msg)
        s.send(msg.encode())

def threadsendmsg():
    th = threading.Thread(target=sendmsg)
    th.start()

startchatimage = PhotoImage(file='start.png')

buttons = Button(root, image=startchatimage, command=func, borderwidth=0)
buttons.place(x=90, y=10)

message = StringVar()
messagebox = Entry(root, textvariable=message, font=('calibre', 10, 'normal'), border=2, width=32)
messagebox.place(x=10, y=444)

sendmessageimg = PhotoImage(file='send.png')

sendmessagebutton = Button(root, image=sendmessageimg, command=threadsendmsg, borderwidth=0)
sendmessagebutton.place(x=260, y=440)

lstbx = Listbox(root, height=20, width=43)
lstbx.place(x=15, y=80)

user_name = Label(root, text=" Number", width=10)

root.mainloop()