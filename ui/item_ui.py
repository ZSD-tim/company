# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:/FatherProject/ui\item.ui'
#
# Created: Wed Feb 10 07:53:07 2021
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Item(object):
    def setupUi(self, Item):
        Item.setObjectName("Item")
        Item.resize(377, 64)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Item)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(Item)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.Package_Combo = QtWidgets.QComboBox(Item)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Package_Combo.sizePolicy().hasHeightForWidth())
        self.Package_Combo.setSizePolicy(sizePolicy)
        self.Package_Combo.setObjectName("Package_Combo")
        self.horizontalLayout.addWidget(self.Package_Combo)
        self.label_4 = QtWidgets.QLabel(Item)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.Customer_Combo = QtWidgets.QComboBox(Item)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Customer_Combo.sizePolicy().hasHeightForWidth())
        self.Customer_Combo.setSizePolicy(sizePolicy)
        self.Customer_Combo.setObjectName("Customer_Combo")
        self.horizontalLayout.addWidget(self.Customer_Combo)
        self.Del_BTN = QtWidgets.QPushButton(Item)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Del_BTN.sizePolicy().hasHeightForWidth())
        self.Del_BTN.setSizePolicy(sizePolicy)
        self.Del_BTN.setMaximumSize(QtCore.QSize(24, 24))
        self.Del_BTN.setStyleSheet("background:red")
        self.Del_BTN.setObjectName("Del_BTN")
        self.horizontalLayout.addWidget(self.Del_BTN)

        self.retranslateUi(Item)
        QtCore.QMetaObject.connectSlotsByName(Item)

    def retranslateUi(self, Item):
        Item.setWindowTitle(QtWidgets.QApplication.translate("Item", "Form", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Item", "封装", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Item", "客户", None, -1))
        self.Del_BTN.setText(QtWidgets.QApplication.translate("Item", "X", None, -1))

