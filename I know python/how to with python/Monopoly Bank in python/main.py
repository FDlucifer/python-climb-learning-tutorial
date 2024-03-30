from tkinter import *

root = Tk()
root.geometry('400x400')
root.resizable(False, False)

namelist = []
number = 0

def score(screen, namelist, money, inittial_money, name, buyorsell, amount):
    #print(money)
    index = namelist.index(name)
    if buyorsell == "ADD":
        amountadded = int(money[index]) + int(amount)
        money[index] = amountadded
    elif buyorsell == "DEDUCT":
        amountadded = int(money[index]) - int(amount)
        money[index] = amountadded
    placey = 80
    for i in money:
        moneydroplabel = Label(screen, text=i, font="bold, 16")
        moneydroplabel.place(x=200, y=placey)

        placey = placey + 35

def submit(numberofplayer):
    #print(numberofplayer)
    global namelist
    global number
    if name.get() != '':
        namelist.append(name.get())
        number = number + 1
        if number == int(numberofplayer):
            root.destroy()
            gamescreen(namelist)

def gamescreen(namelist):
    #print(namelist)
    screen = Tk()
    screen.geometry("350x550")
    screen.resizable(False, False)

    titlelabel = Label(screen, text="Monopoly Bank", font="bold, 20")
    titlelabel.place(x=110, y=14)

    placey = 80
    inittial_money = 30000
    money = []
    for i in namelist:
        money.append(inittial_money)

    for j in namelist:
        namedroplabels = Label(screen, text=j, font="bold, 16")
        namedroplabels.place(x=20, y=placey)

        moneydroplabel = Label(screen, text=inittial_money, font="bold, 16")
        moneydroplabel.place(x=200, y=placey)

        placey = placey + 35

    namedropdownlabel = Label(screen, text="select player", font="bold, 11")
    namedropdownlabel.place(x=20, y=432)

    selectedname = StringVar()
    selectedname.set("player name")
    drop = OptionMenu(screen, selectedname, *namelist)
    drop.place(x=160, y=420)

    buyorsellLabel = Label(screen, text="enter option", font="bold, 11")
    buyorsellLabel.place(x=20, y=453)

    buyorsell = StringVar()
    buyorsell.set("select option")
    buysorsell = ["ADD", "DEDUCT"]
    buyorsells = OptionMenu(screen, buyorsell, *buysorsell)
    buyorsells.place(x=160, y=450)

    amoutLabel = Label(screen, text="amout", font="bold, 11")
    amoutLabel.place(x=20, y=480)

    amout = Entry(screen, borderwidth=5, highlightthickness=0)
    amout.place(x=160, y=485, width=110, height=25)

    button = Button(screen, text="submit", command=lambda:score(screen, namelist, money, inittial_money, selectedname.get(), buyorsell.get(), amout.get()), border=1, height=1, width=14)
    button.place(x=150, y=520)

    screen.mainloop()

titlelabel = Label(root, text="Monopoly Bank", font="bold, 20")
titlelabel.place(x=110, y=14)

numberofplayerlabel = Label(root, text="number of players", font="bold, 16")
numberofplayerlabel.place(x=20, y=80)

numberofplayer = Entry(root, borderwidth=5)
numberofplayer.place(x=200, y=80, width=185, height=33)

namelabel = Label(root, text="enter name", font="bold, 16")
namelabel.place(x=80, y=120)

name = Entry(root, borderwidth=5)
name.place(x=200, y=120, width=185, height=33)

button = Button(root, text="submit", command=lambda:submit(numberofplayer.get()), border=1, height=2, width=20)
button.place(x=150, y=160)

root.mainloop()