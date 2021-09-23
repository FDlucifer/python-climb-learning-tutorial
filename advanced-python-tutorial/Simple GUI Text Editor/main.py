# pip install PyQt5

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import uic

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('editor.ui', self)
        self.show()

        self.setWindowTitle("lUc1f3r11 notepad clone")
        self.action12pt.triggered.connect(lambda: self.change_size(12))
        self.action18pt.triggered.connect(lambda: self.change_size(18))
        self.action24pt.triggered.connect(lambda: self.change_size(24))

        self.actionopen.triggered.connect(self.open_file)
        self.actionsave.triggered.connect(self.save_file)
        self.actionclose.triggered.connect(exit)

    def change_size(self, size):
        self.plainTextEdit.setFont(QFont("Arial", size))

    def open_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "open file", "", "text files (*.txt);;python files (*.py)", options=options)
        if filename != "":
            with open(filename, "r") as f:
                self.plainTextEdit.setPlainText(f.read())

    def save_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "save file", "", "text files (*.txt);;python files (*.py);;all files (*)", options=options)
        if filename != "":
            with open(filename, "w") as f:
                f.write(self.plainTextEdit.toPlainText())

    def close_event(self, event):
        dialog = QMessageBox()
        dialog.setText("do you want to save your work?")
        dialog.addButton(QPushButton("yes"), QMessageBox.YesRole)       # 0
        dialog.addButton(QPushButton("no"), QMessageBox.NoRole)         # 1
        dialog.addButton(QPushButton("cancel"), QMessageBox.RejectRole) # 2

        answer = dialog.exec_()

        if answer == 0:
            self.save_file()
            event.accept()
        elif answer == 2:
            event.ignore()

def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == '__main__':
    main()