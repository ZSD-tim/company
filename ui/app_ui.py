# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\FatherProject\ui\app.ui'
#
# Created: Mon Feb  8 18:20:20 2021
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.West)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Add_BTN = QtWidgets.QPushButton(self.tab)
        self.Add_BTN.setObjectName("Add_BTN")
        self.horizontalLayout_2.addWidget(self.Add_BTN)
        self.Send_BTN = QtWidgets.QPushButton(self.tab)
        self.Send_BTN.setObjectName("Send_BTN")
        self.horizontalLayout_2.addWidget(self.Send_BTN)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.scrollArea = QtWidgets.QScrollArea(self.tab)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.Group_Container = QtWidgets.QWidget()
        self.Group_Container.setGeometry(QtCore.QRect(0, 0, 337, 225))
        self.Group_Container.setObjectName("Group_Container")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Group_Container)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(20, 204, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.scrollArea.setWidget(self.Group_Container)
        self.verticalLayout_2.addWidget(self.scrollArea)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout.addWidget(self.tabWidget)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.Add_BTN.setText(QtWidgets.QApplication.translate("Form", "添加邮件组", None, -1))
        self.Send_BTN.setText(QtWidgets.QApplication.translate("Form", "立即发送邮件", None, -1))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtWidgets.QApplication.translate("Form", "定时发送邮件", None, -1))

