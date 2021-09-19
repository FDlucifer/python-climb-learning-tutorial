# pip install PyQt5

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

def main():
    app = QApplication([])
    window = QWidget()
    window.setGeometry(100, 100, 200, 300)
    window.setWindowTitle("my simple gui")

    layout = QVBoxLayout()

    label = QLabel("press the button below")
    textbox = QTextEdit()
    button = QPushButton("press me!")

    button.clicked.connect(lambda: on_clicked(textbox.toPlainText()))

    layout.addWidget(label)
    layout.addWidget(textbox)
    layout.addWidget(button)
    
    window.setLayout(layout)

    window.show()
    app.exec_()

def on_clicked(msg):
    print("fuck the world!")
    message = QMessageBox()
    message.setText(msg)
    message.exec_()

if __name__ == '__main__':
    main()