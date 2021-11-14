# pip install pyqt5

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem
from PyQt5 import uic
import pickle

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("todogui.ui", self)
        self.show()

        self.setFixedSize(593, 438)
        self.setWindowTitle("lUc1f3r11 ultimate todo v0.1 alpha")
        self.model = QStandardItemModel()
        self.listView.setModel(self.model)

        self.plusButton.clicked.connect(self.add_todo)
        self.minusButton.clicked.connect(self.remove_todo)
        self.actionLoad.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)

    def add_todo(self):
        todo, confirmed = QInputDialog.getText(self, "add todo", "new todo:", QLineEdit.Normal, "")
        if confirmed and not todo.isspace():
            item = QStandardItem(todo)
            self.model.appendRow(item)

    def remove_todo(self):
        if len(self.listView.selectedIndexes()) != 0:
            selected = self.listView.selectedIndexes()[0]

            dialog = QMessageBox()
            dialog.setText(f"do you really want to remove '{selected.data()}'?")
            dialog.addButton(QPushButton("yes"), QMessageBox.YesRole)
            dialog.addButton(QPushButton("no"), QMessageBox.NoRole)
            
            if dialog.exec_() == 0:
                self.model.removeRow(selected.row())

    def open_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "Open File", "", "todo files (*.todo)", options=options)
        if filename != "":
            with open(filename, "rb") as f:
                item_list = pickle.load(f)
                self.model = QStandardItemModel()
                self.listView.setModel(self.model)
                for item in item_list:
                    self.model.appendRow(QStandardItem(item))

    def save_file(self):
        item_list = []
        for x in range(self.model.rowCount()):
            item_list.append(self.model.item(x).text())
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "Save File", "", "todo files (*.todo)", options=options)
        if filename != "":
            with open(filename, "wb") as f:
                pickle.dump(item_list, f)

app = QApplication([])
window = MyGUI()
app.exec_()