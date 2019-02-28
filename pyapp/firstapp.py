from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

from searching import *

import os
import sys


class Search(QMainWindow):
    def __init__(self):
        super(Search,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Search.clicked.connect(self.rooting)
        self.show()


    def rooting(self):
        for roots, directories, files in os.walk("."):
            last_folder = (os.path.basename(roots))
            search_word = self.ui.seachtext.text()
            if search_word in last_folder:
                first_part = os.path.abspath(".")
                sec_part = roots
                paths = os.path.normpath(os.path.join(first_part, sec_part))
                self.ui.searchlist.addItem(paths)


app = QApplication(sys.argv)
widget = Search()
widget.show()
app.exec_()