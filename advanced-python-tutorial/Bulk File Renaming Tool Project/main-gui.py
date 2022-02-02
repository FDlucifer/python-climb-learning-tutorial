# pip install --upgrade --user pyqtwebengine
# pip install --upgrade --user pyqt5

import os
import re

from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import *
from PyQt5 import uic
from itsdangerous import exc
from numpy import sort

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('bulkgui.ui', self)
        self.show()

        self.directory = "."
        self.listModel = QStandardItemModel()
        self.selectModel = QStandardItemModel()

        self.selectView.setModel(self.selectModel)
        self.selected = []

        self.actionOpen.triggered.connect(self.load_directory)
        self.filterButton.clicked.connect(self.filter_list)
        self.selectButton.clicked.connect(self.choose_selection)
        self.removeButton.clicked.connect(self.remove_selection)
        self.applyButton.clicked.connect(self.rename_files)

    def load_directory(self):
        try:
            self.directory = QFileDialog.getExistingDirectory(self, "Select Directory")
            for file in os.listdir(self.directory):
                if os.path.isfile(os.path.join(self.directory, file)):
                    self.listModel.appendRow(QStandardItem(file))
            self.listView.setModel(self.listModel)
        except Exception as e:
            print(e)

    def rename_files(self):
        counter = 1
        try:
            for filename in self.selected:
                if self.addPrefixRadio.isChecked():
                    os.rename(os.path.join(self.directory, filename), os.path.join(self.directory, self.nameEdit.text() + filename))
                elif self.removePrefixRadio.isChecked():
                    if filename.startswith(self.nameEdit.text()):
                        os.rename(os.path.join(self.directory, filename), os.path.join(self.directory, self.filename[len(self.nameEdit.text()):]))
                elif self.addSuffixRadio.isChecked():
                    filetype = filename.split('.')[-1]
                    os.rename(os.path.join(self.directory, filename), os.path.join(self.directory, filename[:-(len(filetype) + 1)] + self.nameEdit.text() + '.' + filetype))
                elif self.removeSuffixRadio.isChecked():
                    filetype = filename.split('.')[-1]
                    if filename.endswith(self.nameEdit.text() + '.' + filetype):
                        os.rename(os.path.join(self.directory, filename), os.path.join(self.directory, filename[:-len(self.nameEdit.text() + '.' + filetype)] + "." + filetype))
                elif self.newNameRadio.isChecked():
                    filetype = filename.split('.')[-1]
                    os.rename(os.path.join(self.directory, filename), os.path.join(self.directory, self.nameEdit.text() + str(counter) + "." + filetype))
                    counter += 1
                else:
                    print("select a radio button!")

                self.selected = []
                self.selectModel.clear()
                self.listModel.clear()

                for file in os.listdir(self.directory):
                    if os.path.isfile(os.path.join(self.directory, file)):
                        self.listModel.appendRow(QStandardItem(file))
                self.listView.setModel(self.listModel)
        except Exception as e:
            print(e)


    def choose_selection(self):
        if len(self.listView.selectedIndexes()) != 0:
            for index in self.listView.selectedIndexes():
                if index.data() not in self.selected:
                    self.selected.append(index.data())
                    self.selectModel.appendRow(QStandardItem(index.data()))

    def remove_selection(self):
        try:
            if len(self.selectView.selectedIndexes()) != 0:
                for index in reversed(sorted(self.selectView.selectedIndexes())):
                    self.selected.remove(index.data())
                    self.selectModel.removeRow(index.row())
        except Exception as e:
            print(e)

    def filter_list(self):
        self.selectModel.clear()
        self.selected = []
        for index in range(self.listModel.rowCount()):
            item = self.listModel.item(index)
            if re.match(self.filterEdit.text(), item.text()):
                self.selectModel.appendRow(QStandardItem(item.text()))
                self.selected.append(item.text())

app = QApplication([])
window = MyGUI()
app.exec_()