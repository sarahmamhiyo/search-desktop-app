# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'search.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 554)
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Search = QtWidgets.QPushButton(self.centralwidget)
        self.Search.setGeometry(QtCore.QRect(140, 210, 131, 31))
        self.Search.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.Search.setMouseTracking(True)
        self.Search.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.Search.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.Search.setStyleSheet("QPushButton{\n"
"    color: #ffffff;\n"
"    font-size:18px;\n"
"    border-radius:10px;\n"
"    background-color: rgb(0, 85, 127);\n"
"    \n"
"\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(7, 121, 127);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/searching.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Search.setIcon(icon)
        self.Search.setIconSize(QtCore.QSize(22, 22))
        self.Search.setObjectName("Search")
        self.seachtext = QtWidgets.QLineEdit(self.centralwidget)
        self.seachtext.setGeometry(QtCore.QRect(70, 30, 261, 31))
        self.seachtext.setStyleSheet("    QLineEdit{\n"
"font-size:16px;\n"
"color:#00557f;\n"
"border: 1px solid #cccccc;\n"
"\n"
"}")
        self.seachtext.setAlignment(QtCore.Qt.AlignCenter)
        self.seachtext.setObjectName("seachtext")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(110, 120, 181, 23))
        self.progressBar.setStyleSheet("QProgressBar::chunk{\n"
" background-color: #00557f;\n"
" width: 5px;\n"
" margin:0.5px;\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.searchlist = QtWidgets.QListWidget(self.centralwidget)
        self.searchlist.setGeometry(QtCore.QRect(490, 270, 256, 192))
        self.searchlist.setObjectName("searchlist")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuSearchBy = QtWidgets.QMenu(self.menubar)
        self.menuSearchBy.setObjectName("menuSearchBy")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionsettings = QtWidgets.QAction(MainWindow)
        self.actionsettings.setObjectName("actionsettings")
        self.actionHistory = QtWidgets.QAction(MainWindow)
        self.actionHistory.setObjectName("actionHistory")
        self.actionFile_Name = QtWidgets.QAction(MainWindow)
        self.actionFile_Name.setObjectName("actionFile_Name")
        self.actionFile_Content = QtWidgets.QAction(MainWindow)
        self.actionFile_Content.setObjectName("actionFile_Content")
        self.actionDelete_Search_History = QtWidgets.QAction(MainWindow)
        self.actionDelete_Search_History.setObjectName("actionDelete_Search_History")
        self.actionSearch_History = QtWidgets.QAction(MainWindow)
        self.actionSearch_History.setObjectName("actionSearch_History")
        self.menuSearchBy.addAction(self.actionHistory)
        self.menuSearchBy.addAction(self.actionFile_Name)
        self.menuSearchBy.addAction(self.actionFile_Content)
        self.menuSettings.addAction(self.actionDelete_Search_History)
        self.menuView.addAction(self.actionSearch_History)
        self.menubar.addAction(self.menuSearchBy.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Easy Search"))
        self.Search.setText(_translate("MainWindow", "Search"))
        self.seachtext.setPlaceholderText(_translate("MainWindow", "Search Content......."))
        self.menuSearchBy.setTitle(_translate("MainWindow", "SearchBy..."))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.actionsettings.setText(_translate("MainWindow", "settings"))
        self.actionHistory.setText(_translate("MainWindow", "History"))
        self.actionFile_Name.setText(_translate("MainWindow", "File Name"))
        self.actionFile_Content.setText(_translate("MainWindow", "File Content"))
        self.actionDelete_Search_History.setText(_translate("MainWindow", "Delete Search History"))
        self.actionSearch_History.setText(_translate("MainWindow", "Search History"))


import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
