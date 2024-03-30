# pip install twilio

from twilio.rest import Client
import random
from tkinter import *
from tkinter import messagebox

class otp_verifier(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x550")
        self.resizable(False, False)
        self.n = random.randint(1000, 9999)
        self.client = Client("", "")
        self.client.messages.create(to = [""],
                                    from_ = "",
                                    body=self.n)

    def Labels(self):
        self.c = Canvas(self, bg = "white", width=400, height=280)
        self.c.place(x=100, y=60)

        self.Login_Title = Label(self, text="OTP Verification", font="bold, 20", bg="white") # login title on top
        self.Login_Title.place(x=210, y=90)

    def Entry(self):
        self.User_Name = Text(self, borderwidth=2, wrap="word", width=29, height=2)
        self.User_Name.place(x=190, y=100)

    def Buttons(self):
        self.submitButtonImage = PhotoImage(file="submit.jpg")
        self.submitButton = Button(self, image=self.submitButtonImage, command=self.checkOTP, border=0)
        self.submitButton.place(x=208, y=240)

        self.resendOTPImage = PhotoImage(file="resendotp.jpg")
        self.resendOTP = Button(self, image=self.resendOTPImage, command=self.resendOTP, border=0)
        self.resendOTP.place(x=208, y=400)

    def checkOTP(self):
        try:
            self.userInput = int(self.User_Name.get(1.0, "end-1c"))
            if self.userInput == self.n:
                messagebox.showinfo("showinfo", "Login Success")
                self.n = "done"
            elif self.n == "done":
                messagebox.showinfo("showinfo", "already Entered the OTP")
            else:
                messagebox.showinfo("showinfo", "wrong OTP")
        except:
            messagebox.showinfo("showinfo", "INVALID OTP")

    def resendOTP(self):
        self.n = random.randint(1000, 9999)
        self.client = Client("", "")
        self.client.messages.create(to = [""],
                                    from_ = "",
                                    body=self.n)

if __name__ == "__main__":
    window = otp_verifier()
    window.Labels()
    window.Entry()
    window.Buttons()
    window.mainloop()