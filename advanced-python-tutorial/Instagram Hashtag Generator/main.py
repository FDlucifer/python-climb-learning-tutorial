# pip install pyqt5

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import uic
from PyQt5.Qt import QStandardItemModel, QStandardItem

import json
import pickle

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi('hashtaggui.ui', self)
        self.show()

        self.setWindowTitle("luc1f3r11 hashtag generator")
        self.hashtag_dict = json.load(open('hashtags.json'))
        self.init_tree_view()

        self.selected = []

        self.list_model = QStandardItemModel()
        self.listView.setModel(self.list_model)

        self.pushButton.clicked.connect(self.copy_to_clipboard)
        self.pushButton_2.clicked.connect(self.choose_selected)
        self.pushButton_3.clicked.connect(self.remove_selected)

        self.actionLoad.triggered.connect(self.load_hashtags)
        self.actionSave.triggered.connect(self.save_hashtags)

    def init_tree_view(self):
        self.treeView.setHeaderHidden(True)

        self.tree_model = QStandardItemModel()
        self.treeView.setModel(self.tree_model)

        root_node = self.tree_model.invisibleRootItem()

        for category in self.hashtag_dict.keys():
            category_item = QStandardItem(category)
            for hashtag in self.hashtag_dict[category]:
                category_item.appendRow(QStandardItem(hashtag))
            root_node.appendRow(category_item)
        
        self.treeView.expandAll()

    def choose_selected(self):
        if len(self.treeView.selectedIndexes()) != 0:
            for index in self.treeView.selectedIndexes():
                if index.parent().isValid():
                    if index.data() not in self.selected:
                        self.selected.append(index.data())
                        self.list_model.appendRow(QStandardItem(index.data()))

    def remove_selected(self):
        if len(self.listView.selectedIndexes()) != 0:
            for index in reversed(sorted(self.listView.selectedIndexes())):
                self.selected.remove(index.data())
                self.list_model.removeRow(index.row())

    def copy_to_clipboard(self):
        if (len(self.selected) != 0):
            clipboard = QApplication.clipboard()
            clipboard.setText('#' + ' #'.join(self.selected))

    def save_hashtags(self):
        filename, confirmed = QFileDialog.getSaveFileName(self, 'save hashtags', '', 'tag file (*.tags)')
        if confirmed:
            with(open(filename, 'wb')) as f:
                pickle.dump(self.selected, f)

    def load_hashtags(self):
        filename, confirmed = QFileDialog.getOpenFileName(self, 'load hashtags', '', 'tag file (*.tags)')
        if confirmed:
            with(open(filename, 'rb')) as f:
                self.selected = pickle.load(f)
            self.list_model = QStandardItemModel()
            for tag in self.selected:
                self.list_model.appendRow(QStandardItem(tag))
            self.listView.setModel(self.list_model)

app = QApplication([])
window = MyGUI()
app.exec_()