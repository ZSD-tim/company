# -*- coding: utf-8 -*-
"""

"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

__author__ = "timmyliang"
__email__ = "820472580@qq.com"
__date__ = "2021-02-08 15:13:33"

from PySide2 import QtCore, QtWidgets, QtGui
from shiboken2 import isValid

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from ui import app_ui
from ui import group_ui
from ui import item_ui

from QBinder import BinderTemplate
from QBinder.eventhook import QEventHook

event_hook = QEventHook.instance()


class ItemBinder(BinderTemplate):
    def __init__(self):
        dumper = self("dumper")
        dumper.set_auto_load(False)
        self.enabled = True


class MailItem(QtWidgets.QWidget, item_ui.Ui_Item):

    update_requested = QtCore.Signal()

    def __init__(self):
        super(MailItem, self).__init__()
        self.setupUi(self)
        self.state = ItemBinder()

        self.Del_BTN.clicked.connect(self.delete_item)

    def delete_item(self):
        self.update_requested.emit()
        self.deleteLater()


class GroupBinder(BinderTemplate):
    def __init__(self):
        dumper = self("dumper")
        dumper.set_auto_load(False)
        self.enabled = True
        self.title = "邮件组"


class MailGroupWidget(QtWidgets.QWidget, group_ui.Ui_Group):

    update_requested = QtCore.Signal()

    def __init__(self):
        super(MailGroupWidget, self).__init__()
        self.setupUi(self)

        self.state = GroupBinder()
        self.Mail_Group.setChecked(lambda: self.state.enabled)
        self.item_list = []

        # NOTE 初始化时间
        self.Send_Time.setTime(QtCore.QTime.currentTime())
        self.Del_BTN.clicked.connect(self.delete_group)
        self.Add_BTN.clicked.connect(self.add_item)

        self.title_edit = QtWidgets.QLineEdit(self)
        self.title_edit.hide()
        self.Mail_Group.setTitle(lambda: self.state.title)
        self.title_edit.setText(lambda: self.state.title)
        self.title_edit.editingFinished.connect(self.title_edit.hide)
        self.title_edit.setFixedWidth(self.Mail_Group.width() + 15)

        self.Mail_Group >> event_hook("MouseButtonDblClick", self.rename_title)
        self.Mail_Group >> event_hook(
            "Resize",
            lambda: self.title_edit.setFixedWidth(self.Mail_Group.width() + 15),
        )

    def rename_title(self):
        self.title_edit.show()
        self.title_edit.selectAll()
        self.title_edit.setFocus()

    def delete_group(self):
        self.update_requested.emit()
        self.deleteLater()

    def add_item(self):
        item = MailItem()
        self.item_list.append(item)
        layout = self.Item_Container.layout()
        layout.addWidget(item)
        item.update_requested.connect(self.update_requested.emit)
        self.update_requested.emit()


class MailWindow(app_ui.Ui_Form, QtWidgets.QWidget):

    message_requested = QtCore.Signal(
        [str, str],
        [str, str, QtWidgets.QSystemTrayIcon.MessageIcon],
        [str, str, QtWidgets.QSystemTrayIcon.MessageIcon, int],
    )

    def __init__(self):
        super(MailWindow, self).__init__()
        self.setupUi(self)
        self.Add_BTN.clicked.connect(self.add_group)
        self.group_list = []

    def add_group(self):
        group = MailGroupWidget()
        self.group_list.append(group)
        layout = self.Group_Container.layout()
        layout.insertWidget(layout.count() - 1, group)

        group.update_requested.connect(
            lambda: QtCore.QTimer.singleShot(100, self.update_data)
        )

    def update_data(self):
        # TODO dump data
        # NOTE 清理已经删除的对象
        QtWidgets.QApplication.processEvents()
        self.group_list = [grp for grp in self.group_list if isValid(grp)]
        for grp in self.group_list:
            grp.item_list = [item for item in grp.item_list if isValid(item)]
            for item in grp.item_list:
                print(item)

    def send_mail(self):
        sender = "13828045672@163.com"
        receivers = ["820472580@qq.com"]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

        # 创建一个带附件的实例
        message = MIMEMultipart()
        message["From"] = Header("菜鸟教程", "utf-8")
        message["To"] = Header("测试", "utf-8")
        message["Subject"] = Header("Python SMTP 邮件测试", "utf-8")

        # 邮件正文内容
        # message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))

        # 构造附件1，传送当前目录下的 test.txt 文件
        att1 = MIMEText(open("test.txt", "rb").read(), "base64", "utf-8")
        att1["Content-Type"] = "application/octet-stream"
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="test.txt"'
        message.attach(att1)

        try:
            smtpObj = smtplib.SMTP("localhost")
            smtpObj.sendmail(sender, receivers, message.as_string())
            self.message_requested.emit("恭喜你", "邮件发送成功")
        except smtplib.SMTPException:
            self.message_requested.emit(
                "错误", "邮件发送失败", QtWidgets.QSystemTrayIcon.Critical
            )
