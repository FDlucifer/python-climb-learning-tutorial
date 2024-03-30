# pip install pillow

import time
import threading
from tkinter import *
import random
import os
from PIL import Image, ImageTk
from tkinter import messagebox

class gameclass(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("850x600")
        self.config(bg="white")
        self.number = 0
        self.number_list = []
        self.random_character = ""
    
    def Label(self):
        self.Label1 = Label(self, text="", font=("times", 30), bg='white')
        self.Label1.place(x=274, y=450)
        
        self.random_character_label = Label(self, text="", font=("times", 30), bg='white')
        self.Label1.place(x=274, y=450)

        self.button1 = Button(self, image="", command=lambda:self.check(1), borderwidth=1, height=5, width=17)
        self.button1.place(x=280, y=20)

        self.button2 = Button(self, image="", command=lambda:self.check(2), borderwidth=1, height=5, width=17)
        self.button2.place(x=450, y=20)

        self.button3 = Button(self, image="", command=lambda:self.check(3), borderwidth=1, height=5, width=17)
        self.button3.place(x=630, y=20)

        self.button4 = Button(self, image="", command=lambda:self.check(4), borderwidth=1, height=5, width=17)
        self.button4.place(x=280, y=150)

        self.button5 = Button(self, image="", command=lambda:self.check(5), borderwidth=1, height=5, width=17)
        self.button5.place(x=450, y=150)

        self.button6 = Button(self, image="", command=lambda:self.check(6), borderwidth=1, height=5, width=17)
        self.button6.place(x=630, y=150)

        self.button7 = Button(self, image="", command=lambda:self.check(7), borderwidth=1, height=5, width=17)
        self.button7.place(x=280, y=280)

        self.button8 = Button(self, image="", command=lambda:self.check(8), borderwidth=1, height=5, width=17)
        self.button8.place(x=450, y=280)

        self.button9 = Button(self, image="", command=lambda:self.check(9), borderwidth=1, height=5, width=17)
        self.button9.place(x=630, y=280)

        self.showbutton = Button(self, text="show", command=self.start_shuffle, borderwidth=0, height=5, width=17)
        self.showbutton.place(x=40, y=150)

    def start_shuffle(self):
        #self.number_list = []
        if (self.number % 2) == 0:
            self.number_list = os.listdir('.')
            self.number_list.remove("main.py")
            self.number_list.remove("blank.png")
            random.shuffle(self.number_list)
            self.img1 = ImageTk.PhotoImage(Image.open(self.number_list[0]))
            self.button1 = Button(self, image=self.img1, command=lambda:self.check(1))
            self.button1.place(x=280, y=20)

            self.img2 = ImageTk.PhotoImage(Image.open(self.number_list[1]))
            self.button2 = Button(self, image=self.img2, command=lambda:self.check(2))
            self.button2.place(x=450, y=20)

            self.img3 = ImageTk.PhotoImage(Image.open(self.number_list[2]))
            self.button3 = Button(self, image=self.img3, command=lambda:self.check(3))
            self.button3.place(x=630, y=20)

            self.img4 = ImageTk.PhotoImage(Image.open(self.number_list[3]))
            self.button4 = Button(self, image=self.img4, command=lambda:self.check(4))
            self.button4.place(x=280, y=150)

            self.img5 = ImageTk.PhotoImage(Image.open(self.number_list[4]))
            self.button5 = Button(self, image=self.img5, command=lambda:self.check(5))
            self.button5.place(x=450, y=150)

            self.img6 = ImageTk.PhotoImage(Image.open(self.number_list[5]))
            self.button6 = Button(self, image=self.img6, command=lambda:self.check(6))
            self.button6.place(x=630, y=150)

            self.img7 = ImageTk.PhotoImage(Image.open(self.number_list[6]))
            self.button7 = Button(self, image=self.img7, command=lambda:self.check(7))
            self.button7.place(x=280, y=280)

            self.img8 = ImageTk.PhotoImage(Image.open(self.number_list[7]))
            self.button8 = Button(self, image=self.img8, command=lambda:self.check(8))
            self.button8.place(x=450, y=280)

            self.img9 = ImageTk.PhotoImage(Image.open(self.number_list[8]))
            self.button9 = Button(self, image=self.img9, command=lambda:self.check(9))
            self.button9.place(x=630, y=280)

            self.showbutton.config(text="Hide")
            self.number = self.number + 1
            self.Label1.destroy()
            self.random_character_label.destroy()

            return self.number

        else:
            self.random_character = random.choice(self.number_list)
            self.imgbtn = ImageTk.PhotoImage(Image.open("blank.png"))
            self.showbutton.config(text="Show")
            self.button1.config(image=self.imgbtn)
            self.button2.config(image=self.imgbtn)
            self.button3.config(image=self.imgbtn)
            self.button4.config(image=self.imgbtn)
            self.button5.config(image=self.imgbtn)
            self.button6.config(image=self.imgbtn)
            self.button7.config(image=self.imgbtn)
            self.button8.config(image=self.imgbtn)
            self.button9.config(image=self.imgbtn)
            self.Label1 = Label(self, text="Pokemon ", font=("times", 30), bg='white')
            self.Label1.place(x=274, y=450)

            self.random_character_label_image = ImageTk.PhotoImage(Image.open(self.random_character))
            self.random_character_label = Label(self, image=self.random_character_label_image)
            self.random_character_label.place(x=510, y=440)

            self.number = self.number + 1

    def check(self, btnnmbr):
        if self.number_list == []:
            messagebox.showinfo("memeory game", "let's start the game first")
            return
        elif self.random_character == "":
            messagebox.showinfo("memeory game", "let's start the game first")

        elif btnnmbr == 1:
            if self.number_list[0] == self.random_character:
                messagebox.showinfo("memeory game", "correct choice")

        elif btnnmbr == 2:
            if self.number_list[1] == self.random_character:
                messagebox.showinfo("memeory game", "correct choice")

        elif btnnmbr == 3:
            if self.number_list[2] == self.random_character:
                messagebox.showinfo("memeory game", "correct choice")

        elif btnnmbr == 4:
            if self.number_list[3] == self.random_character:
                messagebox.showinfo("memeory game", "correct choice")

        elif btnnmbr == 5:
            if self.number_list[4] == self.random_character:
                messagebox.showinfo("memeory game", "correct choice")

        elif btnnmbr == 6:
            if self.number_list[5] == self.random_character:
                messagebox.showinfo("memeory game", "correct choice")

        elif btnnmbr == 7:
            if self.number_list[6] == self.random_character:
                messagebox.showinfo("memeory game", "correct choice")

        elif btnnmbr == 8:
            if self.number_list[7] == self.random_character:
                messagebox.showinfo("memeory game", "correct choice")

        elif btnnmbr == 9:
            if self.number_list[8] == self.random_character:
                messagebox.showinfo("memeory game", "correct choice")


if __name__ == "__main__":
    Game = gameclass()
    Game.Label()
    Game.mainloop()