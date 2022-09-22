# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfase.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet(u"*{\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.filesL = QListWidget(self.centralwidget)
        self.filesL.setObjectName(u"filesL")
        self.filesL.setFrameShadow(QFrame.Plain)
        self.filesL.setDragDropMode(QAbstractItemView.DragDrop)
        self.filesL.setAlternatingRowColors(False)
        self.filesL.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.filesL.setTextElideMode(Qt.ElideRight)
        self.filesL.setMovement(QListView.Snap)
        self.filesL.setFlow(QListView.TopToBottom)
        self.filesL.setResizeMode(QListView.Fixed)
        self.filesL.setLayoutMode(QListView.SinglePass)
        self.filesL.setViewMode(QListView.ListMode)
        self.filesL.setUniformItemSizes(False)
        self.filesL.setBatchSize(100)
        self.filesL.setWordWrap(True)
        self.filesL.setSelectionRectVisible(False)

        self.verticalLayout.addWidget(self.filesL)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.deletableC = QCheckBox(self.centralwidget)
        self.deletableC.setObjectName(u"deletableC")

        self.horizontalLayout.addWidget(self.deletableC)

        self.name = QComboBox(self.centralwidget)
        self.name.addItem("")
        self.name.addItem("")
        self.name.addItem("")
        self.name.addItem("")
        self.name.addItem("")
        self.name.setObjectName(u"name")

        self.horizontalLayout.addWidget(self.name)

        self.delB = QPushButton(self.centralwidget)
        self.delB.setObjectName(u"delB")
        self.delB.setMinimumSize(QSize(0, 40))

        self.horizontalLayout.addWidget(self.delB)

        self.sort = QPushButton(self.centralwidget)
        self.sort.setObjectName(u"sort")
        self.sort.setMinimumSize(QSize(0, 40))

        self.horizontalLayout.addWidget(self.sort)

        self.mergeB = QPushButton(self.centralwidget)
        self.mergeB.setObjectName(u"mergeB")
        self.mergeB.setMinimumSize(QSize(0, 40))

        self.horizontalLayout.addWidget(self.mergeB)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Jpg to Pdf", None))
        self.deletableC.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u044f\u0442\u044c", None))
        self.name.setItemText(0, QCoreApplication.translate("MainWindow", u"P_", None))
        self.name.setItemText(1, QCoreApplication.translate("MainWindow", u"N_", None))
        self.name.setItemText(2, QCoreApplication.translate("MainWindow", u"R_", None))
        self.name.setItemText(3, QCoreApplication.translate("MainWindow", u"NK_", None))
        self.name.setItemText(4, QCoreApplication.translate("MainWindow", u"RK_", None))

        self.delB.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.delB.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
#endif // QT_CONFIG(shortcut)
        self.sort.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.sort.setShortcut(QCoreApplication.translate("MainWindow", u"Space", None))
#endif // QT_CONFIG(shortcut)
        self.mergeB.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u044a\u0435\u0434\u0438\u043d\u0438\u0442\u044c", None))
#if QT_CONFIG(shortcut)
        self.mergeB.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

