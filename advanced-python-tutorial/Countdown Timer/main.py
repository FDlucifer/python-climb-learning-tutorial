# pip install win10toast
# pip install playsound

import threading
import time
import tkinter as tk
from win10toast import ToastNotifier


class CountdownTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("460x220")
        self.root.title("Countdown Timer")

        self.time_entry = tk.Entry(self.root, font=("Helvetica", 30))
        self.time_entry.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.start_button = tk.Button(self.root, font=("Helvetica", 30), text="Start", command=self.start_thread)
        self.start_button.grid(row=1, column=0, padx=5, pady=5)

        self.stop_button = tk.Button(self.root, font=("Helvetica", 30), text="Stop", command=self.stop)
        self.stop_button.grid(row=1, column=1, padx=5, pady=5)

        self.time_label = tk.Label(self.root, font=("Helvetica", 30), text="Time: 00:00:00")
        self.time_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.stop_loop = False

        self.root.mainloop()

    def start_thread(self):
        t = threading.Thread(target=self.start)
        t.start()

    def start(self):
        self.stop_loop = False

        hours, minutes, seconds = 0, 0, 0

        string_split = self.time_entry.get().split(":")

        if len(string_split) == 3:
            hours = int(string_split[0])
            minutes = int(string_split[1])
            seconds = int(string_split[2])
        elif len(string_split) == 2:
            minutes = int(string_split[0])
            seconds = int(string_split[1])
        elif len(string_split) == 1:
            seconds = int(string_split[0])
        else:
            print("invalid time format")
            return

        full_seconds = hours * 3600 + minutes * 60 + seconds

        while full_seconds > 0 and not self.stop_loop:
            full_seconds -= 1

            minutes, seconds = divmod(full_seconds, 60)
            hours, minutes = divmod(minutes, 60)

            self.time_label.config(text=f"Time: {hours:02d}:{minutes:02d}:{seconds:02d}")
            self.root.update()
            time.sleep(1)

        if not self.stop_loop:
            toast = ToastNotifier()
            toast.show_toast("Countdown Timer", "Time is up!", duration=10)


    def stop(self):
        self.stop_loop = True
        self.time_label.config(text="Text: 00:00:00")

CountdownTimer()