# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDockWidget, QGridLayout, QGroupBox,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTabWidget, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 698)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.adb_tab = QWidget()
        self.adb_tab.setObjectName(u"adb_tab")
        self.gridLayout_2 = QGridLayout(self.adb_tab)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.apk_groupBox = QGroupBox(self.adb_tab)
        self.apk_groupBox.setObjectName(u"apk_groupBox")
        self.verticalLayout_7 = QVBoxLayout(self.apk_groupBox)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.install_apk_pushButton = QPushButton(self.apk_groupBox)
        self.install_apk_pushButton.setObjectName(u"install_apk_pushButton")

        self.verticalLayout_7.addWidget(self.install_apk_pushButton)

        self.uninstall_apk_pushButton = QPushButton(self.apk_groupBox)
        self.uninstall_apk_pushButton.setObjectName(u"uninstall_apk_pushButton")

        self.verticalLayout_7.addWidget(self.uninstall_apk_pushButton)

        self.adb_shell_am_force__stop_package_pushButton = QPushButton(self.apk_groupBox)
        self.adb_shell_am_force__stop_package_pushButton.setObjectName(u"adb_shell_am_force__stop_package_pushButton")

        self.verticalLayout_7.addWidget(self.adb_shell_am_force__stop_package_pushButton)


        self.gridLayout.addWidget(self.apk_groupBox, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)

        self.groupBox = QGroupBox(self.adb_tab)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.adb_devices_pushButton = QPushButton(self.groupBox)
        self.adb_devices_pushButton.setObjectName(u"adb_devices_pushButton")

        self.verticalLayout_5.addWidget(self.adb_devices_pushButton)

        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_5.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.groupBox)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_5.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.groupBox)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_5.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.groupBox)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_5.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.groupBox)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_5.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.groupBox)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_5.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.groupBox)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout_5.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.groupBox)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout_5.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.groupBox)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.verticalLayout_5.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.groupBox)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.verticalLayout_5.addWidget(self.pushButton_11)


        self.gridLayout_2.addWidget(self.groupBox, 0, 0, 1, 1)

        self.tabWidget.addTab(self.adb_tab, "")
        self.frida_tab = QWidget()
        self.frida_tab.setObjectName(u"frida_tab")
        self.verticalLayout_6 = QVBoxLayout(self.frida_tab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.tabWidget.addTab(self.frida_tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 37))
        self.about_menu = QMenu(self.menubar)
        self.about_menu.setObjectName(u"about_menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget = QDockWidget(MainWindow)
        self.dockWidget.setObjectName(u"dockWidget")
        self.log_dockWidgetContents = QWidget()
        self.log_dockWidgetContents.setObjectName(u"log_dockWidgetContents")
        self.verticalLayout_2 = QVBoxLayout(self.log_dockWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.log_groupBox = QGroupBox(self.log_dockWidgetContents)
        self.log_groupBox.setObjectName(u"log_groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.log_groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.log_textBrowser = QTextBrowser(self.log_groupBox)
        self.log_textBrowser.setObjectName(u"log_textBrowser")

        self.verticalLayout_3.addWidget(self.log_textBrowser)


        self.verticalLayout_2.addWidget(self.log_groupBox)

        self.dockWidget.setWidget(self.log_dockWidgetContents)
        MainWindow.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.dockWidget)

        self.menubar.addAction(self.about_menu.menuAction())

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.apk_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u5e94\u7528\u7ba1\u7406", None))
        self.install_apk_pushButton.setText(QCoreApplication.translate("MainWindow", u"adb install <apk>", None))
        self.uninstall_apk_pushButton.setText(QCoreApplication.translate("MainWindow", u"adb uninstall <package>", None))
        self.adb_shell_am_force__stop_package_pushButton.setText(QCoreApplication.translate("MainWindow", u"adb shell am force-stop <package>", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u5907\u7ba1\u7406", None))
        self.adb_devices_pushButton.setText(QCoreApplication.translate("MainWindow", u"adb devices", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"adb get-serialno", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"adb reboot", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"adb reboot bootloader", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"adb reboot recovery", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"adb root", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"adb unroot", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"adb kill-server", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"adb start-server", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"adb connect <ip:port>", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"adb disconnect <ip:port>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.adb_tab), QCoreApplication.translate("MainWindow", u"adb", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.frida_tab), QCoreApplication.translate("MainWindow", u"frida", None))
        self.about_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.log_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7", None))
    # retranslateUi

