# pip install PyQt5

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

# first we do is create a class
class MainWindow(QMainWindow):
    # we create a constructor - python relies on the constructor to perform tasks
    # (assigning values to) any instance variables that the object will need
    def __init__(self):

        # create a super connection with parent class (QMainWindow)
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com/'))
        self.setCentralWidget(self.browser)

        # make browser full screen
        self.showMaximized()

        # navigation
        navbar = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('<-', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('->', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        refresh_btn = QAction('Refresh', self)
        refresh_btn.triggered.connect(self.browser.reload)
        navbar.addAction(refresh_btn)

        myblog_btn = QAction('myblog', self)
        myblog_btn.triggered.connect(self.navigate_myblog)
        navbar.addAction(myblog_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_myblog(self):
        self.browser.setUrl(QUrl('https://fdlucifer.github.io/'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, r):
        self.url_bar.setText(r.toString())

# initialize app and pass system argument
app = QApplication(sys.argv)

# set app name
QApplication.setApplicationName('lucicode chrome')

# Window class that we created above
window = MainWindow()

# call app to execute
app.exec_()