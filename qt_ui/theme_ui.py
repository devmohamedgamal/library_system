# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_ui/theme_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Theme(object):
    def setupUi(self, Theme):
        Theme.setObjectName("Theme")
        Theme.resize(446, 544)
        Theme.setStyleSheet("\n"
"background-color: rgb(236, 236, 236);")
        self.label = QtWidgets.QLabel(Theme)
        self.label.setGeometry(QtCore.QRect(110, 50, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(Theme)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 120, 391, 331))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(0, 150))
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(0, 150))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(0, 150))
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(0, 150))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)

        self.retranslateUi(Theme)
        QtCore.QMetaObject.connectSlotsByName(Theme)

    def retranslateUi(self, Theme):
        _translate = QtCore.QCoreApplication.translate
        Theme.setWindowTitle(_translate("Theme", "Form"))
        self.label.setText(_translate("Theme", "Apply New Theme \"_\""))
        self.pushButton.setText(_translate("Theme", "Clasic"))
        self.pushButton_2.setText(_translate("Theme", "Dark"))
        self.pushButton_3.setText(_translate("Theme", "Vantom"))
        self.pushButton_4.setText(_translate("Theme", "Dark Blue"))
