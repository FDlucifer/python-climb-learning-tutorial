# pip install qrcode opencv-python

import cv2
import sys
import qrcode

from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("qrcodegui.ui", self)
        self.show()

        self.current_file = ""
        self.actionLoad.triggered.connect(self.load_image)
        self.actionSave.triggered.connect(self.save_image)
        self.actionQuit.triggered.connect(self.quit_program)
        self.pushButton.clicked.connect(self.generate_code)
        self.pushButton_2.clicked.connect(self.read_code)

    def load_image(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*)", options=options)

        if filename != "":
            self.current_file = filename
            pixmap = QtGui.QPixmap(self.current_file)
            pixmap = pixmap.scaled(300, 300)
            self.label.setScaledContents(True)
            self.label.setPixmap(pixmap)

    def save_image(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "PNG (*.png)", options=options)

        if filename != "":
            img = self.label.pixmap()
            img.save(filename, "PNG")

    def generate_code(self):
        qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=20, border=2)
        qr.add_data(self.textEdit.toPlainText())
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        img.save("currentqr.png")

        pixmap = QtGui.QPixmap("currentqr.png")
        pixmap = pixmap.scaled(300, 300)
        self.label.setScaledContents(True)
        self.label.setPixmap(pixmap)

    def read_code(self):
        img = cv2.imread(self.current_file)
        detector = cv2.QRCodeDetector()
        data, _, _ = detector.detectAndDecode(img)
        self.textEdit.setText(data)

    def quit_program(self):
        sys.exit(0)

def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == "__main__":
    main()

