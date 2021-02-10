# -*- coding: utf-8 -*-
"""

"""

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

__author__ = "timmyliang"
__email__ = "820472580@qq.com"
__date__ = "2021-02-08 11:24:37"

import signal

signal.signal(signal.SIGINT, signal.SIG_DFL)

import re
import os
import sys
import time
import tempfile
from datetime import datetime

from PySide2 import QtCore, QtWidgets, QtGui
from resources import app_rc
from ui import temp_app_ui

from QBinder import BinderTemplate
from QBinder.handler import Set

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from email.mime.base import MIMEBase
from email import encoders
 

from dumper import DataDumper


class ConfigureBinder(BinderTemplate):
    def __init__(self):
        self.invalid = False
        self.color = "transparent"
        with self("dumper") as dumper:
            self.mail = ""
            self.title = ""
            self.hour = 10
            self.hour2 = 16
            self.minute = 30
            self.minute2 = 30
            self.send = False
            self.send2 = False
        # print(dumper.path)


class ConfigureWidget(temp_app_ui.Ui_Form, QtWidgets.QWidget):
    message_requested = QtCore.Signal(
        [str, str, QtWidgets.QSystemTrayIcon.MessageIcon],
    )

    state = ConfigureBinder()

    def __init__(self):
        super(ConfigureWidget, self).__init__()
        self.setupUi(self)
        self.setting = QtCore.QSettings("TimmyLiang", "CompanyTray")

        self.Mail_LE.setText(lambda: self.state.mail)
        self.Mail_LE.setStyleSheet(lambda: "border: 1px solid %s" % self.state.color)
        self.Validate_Label.setVisible(lambda: self.state.invalid)
        self.Mail_LE.editingFinished.connect(self.validate_mail)

        self.Send_CB.setChecked(lambda: self.state.send)
        self.Send2_CB.setChecked(lambda: self.state.send2)
        self.Hour_SB.setValue(lambda: self.state.hour)
        self.Minute_SB.setValue(lambda: self.state.minute)
        self.Hour2_SB.setValue(lambda: self.state.hour2)
        self.Minute2_SB.setValue(lambda: self.state.minute2)

        self.Title_LE.setText(lambda: self.state.title)
        self.Content_TE.setPlainText(self.setting.value("content", ""))
        self.Content_TE.textChanged.connect(
            lambda: self.setting.setValue("content", self.Content_TE.toPlainText())
        )

        self.Send_BTN.clicked.connect(self.send_email)

    def validate_mail(self):
        mail = self.state.mail
        if not mail:
            return
        reg = r"\A(?P<name>[\w\-_]+)@(?P<domain>[\w\-_]+).(?P<toplevel>[\w]+)\Z"
        match = re.match(reg, mail, re.IGNORECASE)
        if not match:
            self.state.mail = ""
            self.state.invalid = True

        self.state.color = "green" if match else "red"
        QtCore.QTimer.singleShot(
            2000,
            lambda: self.state.color >> Set("transparent")
            if match
            else (
                self.state.invalid >> Set(False),
                self.state.color >> Set("transparent"),
            ),
        )

    def mail_attch(self, path):
        # 构造附件1，传送当前目录下的 test.txt 文件
        att = MIMEText(open(path, "rb").read(), "base64", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        # print(os.path.basename(path))
        att.add_header('Content-Disposition', 'attachment', filename=os.path.basename(path))
        # att["Content-Disposition"] = f'attachment; filename="{os.path.basename(path)}"'
        return att

    @classmethod
    def clean_path(cls,path):
        if os.path.exists(path):
            os.remove(path)
    
    def send_email(self):
        sender = "13828045672@163.com"
        # sender = "tim115wp@163.com"
        smtp_server = "smtp.163.com"
        password = "JLTAFQDKZSNCPIKF"
        receivers = [self.state.mail]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

        # 创建一个带附件的实例
        message = MIMEMultipart()
        message["From"] = Header(sender, "utf-8")
        # message["To"] = Header(receivers[0], "utf-8")
        message["To"] = receivers[0]
        # message["Subject"] = Header(self.state.title, "utf-8")
        message["Subject"] = self.state.title

        # 邮件正文内容
        message.attach(MIMEText(self.setting.value("content", "")))

        directory = tempfile.mkdtemp()

        out_path = os.path.join(directory, "出库报表.xlsx")
        self.clean_path(out_path)
        DataDumper.dump_outcoming(out_path)
        inventory_path = os.path.join(directory, "库存明细.xlsx")
        self.clean_path(inventory_path)
        DataDumper.dump_inventory(inventory_path)
        in_path = os.path.join(directory, "入库报表.xlsx")
        self.clean_path(in_path)
        DataDumper.dump_incoming(in_path)
        progress_path = os.path.join(directory, "生产进度表.xlsx")
        self.clean_path(progress_path)
        DataDumper.dump_progress(progress_path)

        message.attach(self.mail_attch(out_path))
        message.attach(self.mail_attch(inventory_path))
        message.attach(self.mail_attch(in_path))
        message.attach(self.mail_attch(progress_path))

        try:
            smtp = smtplib.SMTP_SSL(smtp_server, 465)
            smtp.login(sender, password)
            smtp.sendmail(sender, receivers, message.as_string())
            self.message_requested.emit(
                "恭喜你", "邮件发送成功", QtWidgets.QSystemTrayIcon.Information
            )
            print("done")
        except smtplib.SMTPException:
            import traceback

            traceback.print_exc()
            self.message_requested.emit(
                "错误",
                "邮件发送失败 %s" % traceback.format_exc(),
                QtWidgets.QSystemTrayIcon.Critical,
            )


class CompanyWindow(ConfigureWidget, QtWidgets.QWidget):
    def __init__(self):
        super(CompanyWindow, self).__init__()

        self.setWindowTitle("公司办公套件")
        self.resize(400, 300)

        self.createTrayIcon()
        self.setIcon(QtGui.QPixmap(":\logo.png"))
        self.tray.activated.connect(self.iconActivated)

        self.tray.show()
        self.message_requested.connect(self.tray.showMessage)
        self.tray.showMessage(
            "提示",
            "办公套件启动成功",
        )

        # NOTE 生成开机启动
        self.auto_startup()

        # NOTE 每 10s 检测发送
        self.timer = QtCore.QTimer()
        self.timer.setInterval(10000)
        self.timer.timeout.connect(self.auto_send)
        self.timer.start()

    def auto_send(self):
        current_date = time.strftime("%Y-%m-%d", time.localtime())
        task = self.setting.value(current_date, {})
        now = datetime.now()
        minute = now.minute
        hour = now.hour

        flag = not task.get("1") or not self.state.send
        if flag and minute >= self.state.minute and hour >= self.state.hour:
            task["1"] = True
            self.setting.setValue(current_date, task)
            self.send_email()

        flag = not task.get("2") or not self.state.send2
        if flag and minute >= self.state.minute2 and hour >= self.state.hour2:
            task["2"] = True
            self.setting.setValue(current_date, task)
            self.send_email()

        self.state.send = task.get("1", False)
        self.state.send2 = task.get("2", False)

    def auto_startup(self):
        RUN_PATH = (
            "HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run"
        )
        self.reg = QtCore.QSettings(RUN_PATH, QtCore.QSettings.NativeFormat)
        self.reg.setValue("CompanySuite", sys.argv[0])

    def setVisible(self, visible):
        self.minimizeAction.setEnabled(visible)
        self.maximizeAction.setEnabled(not self.isMaximized())
        self.restoreAction.setEnabled(self.isMaximized() or not visible)
        super(CompanyWindow, self).setVisible(visible)

    def closeEvent(self, event):
        if self.tray.isVisible():
            self.hide()
            event.ignore()
            # background_run = self.setting.value("background_run",None)
            # if background_run is None:
            #     ret = QtWidgets.QMessageBox.question(self, "提示",
            #         "是否托盘运行程序",
            #         QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No )

            #     background_run = ret == QtWidgets.QMessageBox.Yes
            #     self.setting.setValue("background_run",background_run)
            # if background_run:
            #     self.hide()
            #     event.ignore()

    def setIcon(self, icon, tooltip=""):
        self.tray.setIcon(icon)
        self.setWindowIcon(icon)
        self.tray.setToolTip(tooltip)

    def iconActivated(self, reason):
        if reason in (
            QtWidgets.QSystemTrayIcon.Trigger,
            QtWidgets.QSystemTrayIcon.DoubleClick,
        ):
            self.showNormal()
        # elif reason == QtWidgets.QSystemTrayIcon.MiddleClick:
        #     self.showMessage()

    def createTrayIcon(self):

        self.tray_menu = QtWidgets.QMenu(self)

        self.minimizeAction = QtWidgets.QAction("最小化", self, triggered=self.hide)

        self.maximizeAction = QtWidgets.QAction(
            "最大化", self, triggered=self.showMaximized
        )

        self.restoreAction = QtWidgets.QAction("打开窗口", self, triggered=self.showNormal)
        self.quitAction = QtWidgets.QAction(
            "退出", self, triggered=QtWidgets.QApplication.quit
        )
        self.tray_menu.addAction(self.minimizeAction)
        self.tray_menu.addAction(self.maximizeAction)
        self.tray_menu.addAction(self.restoreAction)
        self.tray_menu.addSeparator()
        self.tray_menu.addAction(self.quitAction)

        self.tray = QtWidgets.QSystemTrayIcon(self)
        self.tray.setContextMenu(self.tray_menu)


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle("Fusion")

    # style = app.style()
    # icon = QtGui.QIcon(style.standardPixmap(QtWidgets.QStyle.SP_ComputerIcon))
    tray = CompanyWindow()
    tray.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()