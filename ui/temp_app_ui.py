# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:/FatherProject/ui\temp_app.ui'
#
# Created: Wed Feb 10 07:53:07 2021
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(455, 304)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.Mail_LE = QtWidgets.QLineEdit(Form)
        self.Mail_LE.setObjectName("Mail_LE")
        self.horizontalLayout.addWidget(self.Mail_LE)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.Validate_Label = QtWidgets.QLabel(Form)
        self.Validate_Label.setStyleSheet("color:red")
        self.Validate_Label.setObjectName("Validate_Label")
        self.verticalLayout.addWidget(self.Validate_Label)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.Send_CB = QtWidgets.QCheckBox(Form)
        self.Send_CB.setObjectName("Send_CB")
        self.horizontalLayout_3.addWidget(self.Send_CB)
        self.Hour_SB = QtWidgets.QSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Hour_SB.sizePolicy().hasHeightForWidth())
        self.Hour_SB.setSizePolicy(sizePolicy)
        self.Hour_SB.setMaximum(24)
        self.Hour_SB.setProperty("value", 9)
        self.Hour_SB.setObjectName("Hour_SB")
        self.horizontalLayout_3.addWidget(self.Hour_SB)
        self.label_3 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.Minute_SB = QtWidgets.QSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Minute_SB.sizePolicy().hasHeightForWidth())
        self.Minute_SB.setSizePolicy(sizePolicy)
        self.Minute_SB.setMaximum(59)
        self.Minute_SB.setProperty("value", 30)
        self.Minute_SB.setObjectName("Minute_SB")
        self.horizontalLayout_3.addWidget(self.Minute_SB)
        self.label_4 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Send2_CB = QtWidgets.QCheckBox(Form)
        self.Send2_CB.setObjectName("Send2_CB")
        self.horizontalLayout_4.addWidget(self.Send2_CB)
        self.Hour2_SB = QtWidgets.QSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Hour2_SB.sizePolicy().hasHeightForWidth())
        self.Hour2_SB.setSizePolicy(sizePolicy)
        self.Hour2_SB.setMaximum(24)
        self.Hour2_SB.setProperty("value", 16)
        self.Hour2_SB.setObjectName("Hour2_SB")
        self.horizontalLayout_4.addWidget(self.Hour2_SB)
        self.label_6 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_4.addWidget(self.label_6)
        self.Minute2_SB = QtWidgets.QSpinBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Minute2_SB.sizePolicy().hasHeightForWidth())
        self.Minute2_SB.setSizePolicy(sizePolicy)
        self.Minute2_SB.setMaximum(59)
        self.Minute2_SB.setProperty("value", 30)
        self.Minute2_SB.setObjectName("Minute2_SB")
        self.horizontalLayout_4.addWidget(self.Minute2_SB)
        self.label_7 = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.Title_LE = QtWidgets.QLineEdit(Form)
        self.Title_LE.setObjectName("Title_LE")
        self.verticalLayout.addWidget(self.Title_LE)
        self.Content_TE = QtWidgets.QPlainTextEdit(Form)
        self.Content_TE.setObjectName("Content_TE")
        self.verticalLayout.addWidget(self.Content_TE)
        self.Send_BTN = QtWidgets.QPushButton(Form)
        self.Send_BTN.setObjectName("Send_BTN")
        self.verticalLayout.addWidget(self.Send_BTN)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtWidgets.QApplication.translate("Form", "Form", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("Form", "目标邮箱", None, -1))
        self.Validate_Label.setText(QtWidgets.QApplication.translate("Form", "请输入合法的邮箱", None, -1))
        self.Send_CB.setText(QtWidgets.QApplication.translate("Form", "发送时间1", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("Form", "时", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("Form", "分", None, -1))
        self.Send2_CB.setText(QtWidgets.QApplication.translate("Form", "发送时间2", None, -1))
        self.label_6.setText(QtWidgets.QApplication.translate("Form", "时", None, -1))
        self.label_7.setText(QtWidgets.QApplication.translate("Form", "分", None, -1))
        self.Title_LE.setPlaceholderText(QtWidgets.QApplication.translate("Form", "邮件标题...", None, -1))
        self.Content_TE.setPlaceholderText(QtWidgets.QApplication.translate("Form", "邮件正文内容...", None, -1))
        self.Send_BTN.setText(QtWidgets.QApplication.translate("Form", "手动发送", None, -1))
