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

import sys

from PySide2 import QtCore, QtWidgets, QtGui
from resources import app_rc
from mail import MailWindow


class CompanyWindow(MailWindow, QtWidgets.QWidget):
    def __init__(self):
        super(CompanyWindow, self).__init__()

        self.setWindowTitle("公司办公套件")
        self.resize(400, 300)

        self.setting = QtCore.QSettings("TimmyLiang", "CompanyTray")

        self.createTrayIcon()
        self.setIcon(QtGui.QPixmap(":\logo.png"))
        self.tray.activated.connect(self.iconActivated)

        self.tray.show()
        self.message_requested.connect(self.tray.showMessage)
        self.tray.showMessage(
            "提示",
            "办公套件启动成功",
        )

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