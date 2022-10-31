# pip install PyQt5 --user

import time
import threading
from PyQt5 import uic
from PyQt5.QtWidgets import *

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("stopwatch.ui", self)
        self.show()

        self.running = False
        self.started = False

        self.passed = 0
        self.previous_passed = 0
        self.lap = 1

        self.pushButton.clicked.connect(self.start_stop)
        self.pushButton_2.clicked.connect(self.lap_reset)
        self.label_2.setStyleSheet("border: 10px solid transparent")

    def start_stop(self):
        if self.running:
            self.running = False
            self.pushButton.setText("Resume")
            self.pushButton_2.setText("Reset")
        else:
            self.running = True
            self.pushButton.setText("Stop")
            self.pushButton_2.setText("Lap")
            self.pushButton_2.setEnabled(True)
            threading.Thread(target=self.stopwatch).start()

    def lap_reset(self):
        if self.running:
            self.label_2.setText(self.label_2.text() + f"(Lap {self.lap} - Passed: {self.format_time_string(self.passed)}"
            f" - Difference: {self.format_time_string(self.passed - self.previous_passed)})")
            self.lap += 1
            self.previous_passed = self.passed
        else:
            self.pushButton.setText("Start")
            self.pushButton_2.setText("Lap")
            self.pushButton_2.setEnabled(False)
            self.label.setText("00:00:00:00")
            self.label_2.setText("Laps: ")
            self.lap = 1
            self.passed = 0
            self.previous_passed = 0

    def format_time_string(self, time_passed):
        secs = time_passed % 60
        mins = time_passed // 60
        hours = mins // 60
        return f"{int(hours):02d}:{int(mins):02d}:{int(secs):02d}:{int((self.passed % 1) * 100):02d}"

    def stopwatch(self):
        start = time.time()
        if self.started:
            until_now = self.passed
        else:
            until_now = 0
            self.started = True

        while self.running:
            self.passed = time.time() - start + until_now
            self.label.setText(self.format_time_string(self.passed))

def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == "__main__":
    main()