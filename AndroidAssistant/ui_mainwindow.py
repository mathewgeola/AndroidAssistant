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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QDockWidget,
    QFrame, QGroupBox, QHBoxLayout, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QMenu, QMenuBar, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1183, 900)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.adb_page = QWidget()
        self.adb_page.setObjectName(u"adb_page")
        self.horizontalLayout_3 = QHBoxLayout(self.adb_page)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_4 = QFrame(self.adb_page)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.scrollArea_5 = QScrollArea(self.frame_4)
        self.scrollArea_5.setObjectName(u"scrollArea_5")
        self.scrollArea_5.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 991, 1053))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.adb_devices_groupBox = QGroupBox(self.scrollAreaWidgetContents_5)
        self.adb_devices_groupBox.setObjectName(u"adb_devices_groupBox")
        self.verticalLayout_11 = QVBoxLayout(self.adb_devices_groupBox)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.adb_devices_listWidget = QListWidget(self.adb_devices_groupBox)
        self.adb_devices_listWidget.setObjectName(u"adb_devices_listWidget")

        self.verticalLayout_11.addWidget(self.adb_devices_listWidget)

        self.frame_3 = QFrame(self.adb_devices_groupBox)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_10 = QFrame(self.frame_3)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_2 = QFrame(self.frame_10)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.long_checkBox_2 = QCheckBox(self.frame_2)
        self.long_checkBox_2.setObjectName(u"long_checkBox_2")

        self.horizontalLayout.addWidget(self.long_checkBox_2)


        self.horizontalLayout_7.addWidget(self.frame_2)

        self.adb_devices_pushButton = QPushButton(self.frame_10)
        self.adb_devices_pushButton.setObjectName(u"adb_devices_pushButton")

        self.horizontalLayout_7.addWidget(self.adb_devices_pushButton)


        self.verticalLayout_8.addWidget(self.frame_10)


        self.verticalLayout_11.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.adb_devices_groupBox)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_11 = QFrame(self.frame_5)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.adb_start_server_pushButton = QPushButton(self.frame_11)
        self.adb_start_server_pushButton.setObjectName(u"adb_start_server_pushButton")

        self.horizontalLayout_4.addWidget(self.adb_start_server_pushButton)

        self.adb_kill_server_pushButton = QPushButton(self.frame_11)
        self.adb_kill_server_pushButton.setObjectName(u"adb_kill_server_pushButton")

        self.horizontalLayout_4.addWidget(self.adb_kill_server_pushButton)


        self.verticalLayout_16.addWidget(self.frame_11)

        self.adb_reboot_pushButton = QPushButton(self.frame_5)
        self.adb_reboot_pushButton.setObjectName(u"adb_reboot_pushButton")

        self.verticalLayout_16.addWidget(self.adb_reboot_pushButton)

        self.adb_reboot_bootloader_pushButton = QPushButton(self.frame_5)
        self.adb_reboot_bootloader_pushButton.setObjectName(u"adb_reboot_bootloader_pushButton")

        self.verticalLayout_16.addWidget(self.adb_reboot_bootloader_pushButton)


        self.verticalLayout_11.addWidget(self.frame_5)


        self.verticalLayout_12.addWidget(self.adb_devices_groupBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_12.addItem(self.horizontalSpacer)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents_5)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.fastboot_devices_listWidget = QListWidget(self.groupBox_4)
        self.fastboot_devices_listWidget.setObjectName(u"fastboot_devices_listWidget")

        self.verticalLayout_17.addWidget(self.fastboot_devices_listWidget)

        self.fastboot_devices_pushButton = QPushButton(self.groupBox_4)
        self.fastboot_devices_pushButton.setObjectName(u"fastboot_devices_pushButton")

        self.verticalLayout_17.addWidget(self.fastboot_devices_pushButton)

        self.frame_8 = QFrame(self.groupBox_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.fastboot_reboot_pushButton = QPushButton(self.frame_8)
        self.fastboot_reboot_pushButton.setObjectName(u"fastboot_reboot_pushButton")

        self.horizontalLayout_9.addWidget(self.fastboot_reboot_pushButton)


        self.verticalLayout_17.addWidget(self.frame_8)


        self.verticalLayout_12.addWidget(self.groupBox_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_12.addItem(self.horizontalSpacer_2)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents_5)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_14 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.adb_shell_pm_list_packages_listWidget = QListWidget(self.groupBox_2)
        self.adb_shell_pm_list_packages_listWidget.setObjectName(u"adb_shell_pm_list_packages_listWidget")
        self.adb_shell_pm_list_packages_listWidget.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        self.verticalLayout_14.addWidget(self.adb_shell_pm_list_packages_listWidget)

        self.frame_6 = QFrame(self.groupBox_2)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_9)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.system_packages_checkBox = QCheckBox(self.frame_9)
        self.system_packages_checkBox.setObjectName(u"system_packages_checkBox")

        self.verticalLayout_5.addWidget(self.system_packages_checkBox)

        self.third_party_packages_checkBox = QCheckBox(self.frame_9)
        self.third_party_packages_checkBox.setObjectName(u"third_party_packages_checkBox")

        self.verticalLayout_5.addWidget(self.third_party_packages_checkBox)


        self.horizontalLayout_5.addWidget(self.frame_9)

        self.adb_shell_pm_list_packages_pushButton = QPushButton(self.frame_6)
        self.adb_shell_pm_list_packages_pushButton.setObjectName(u"adb_shell_pm_list_packages_pushButton")

        self.horizontalLayout_5.addWidget(self.adb_shell_pm_list_packages_pushButton)


        self.verticalLayout_14.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.groupBox_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.install_apk_pushButton = QPushButton(self.frame_7)
        self.install_apk_pushButton.setObjectName(u"install_apk_pushButton")

        self.horizontalLayout_6.addWidget(self.install_apk_pushButton)

        self.uninstall_apk_pushButton = QPushButton(self.frame_7)
        self.uninstall_apk_pushButton.setObjectName(u"uninstall_apk_pushButton")

        self.horizontalLayout_6.addWidget(self.uninstall_apk_pushButton)


        self.verticalLayout_14.addWidget(self.frame_7)


        self.verticalLayout_12.addWidget(self.groupBox_2)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout_12.addItem(self.horizontalSpacer_3)

        self.groupBox_5 = QGroupBox(self.scrollAreaWidgetContents_5)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.verticalLayout_15 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.listWidget = QListWidget(self.groupBox_5)
        self.listWidget.setObjectName(u"listWidget")

        self.verticalLayout_15.addWidget(self.listWidget)

        self.frame = QFrame(self.groupBox_5)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_2.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton)


        self.verticalLayout_15.addWidget(self.frame)

        self.adb_shell_am_force__stop_package_pushButton = QPushButton(self.groupBox_5)
        self.adb_shell_am_force__stop_package_pushButton.setObjectName(u"adb_shell_am_force__stop_package_pushButton")

        self.verticalLayout_15.addWidget(self.adb_shell_am_force__stop_package_pushButton)


        self.verticalLayout_12.addWidget(self.groupBox_5)

        self.scrollArea_5.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_13.addWidget(self.scrollArea_5)


        self.horizontalLayout_3.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.adb_page)
        self.frida_page = QWidget()
        self.frida_page.setObjectName(u"frida_page")
        self.verticalLayout_9 = QVBoxLayout(self.frida_page)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.groupBox = QGroupBox(self.frida_page)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_6 = QVBoxLayout(self.groupBox)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_2 = QPushButton(self.groupBox)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_6.addWidget(self.pushButton_2)


        self.verticalLayout_9.addWidget(self.groupBox)

        self.stackedWidget.addWidget(self.frida_page)

        self.verticalLayout_4.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1183, 21))
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
        self.dockWidget_6 = QDockWidget(MainWindow)
        self.dockWidget_6.setObjectName(u"dockWidget_6")
        self.dockWidgetContents_5 = QWidget()
        self.dockWidgetContents_5.setObjectName(u"dockWidgetContents_5")
        self.verticalLayout = QVBoxLayout(self.dockWidgetContents_5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_6 = QGroupBox(self.dockWidgetContents_5)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.adb_pushButton = QPushButton(self.groupBox_6)
        self.adb_pushButton.setObjectName(u"adb_pushButton")

        self.verticalLayout_7.addWidget(self.adb_pushButton)

        self.frida_pushButton = QPushButton(self.groupBox_6)
        self.frida_pushButton.setObjectName(u"frida_pushButton")

        self.verticalLayout_7.addWidget(self.frida_pushButton)


        self.verticalLayout.addWidget(self.groupBox_6)

        self.dockWidget_6.setWidget(self.dockWidgetContents_5)
        MainWindow.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, self.dockWidget_6)

        self.menubar.addAction(self.about_menu.menuAction())

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.adb_devices_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"ADB \u8bbe\u5907", None))
        self.long_checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u663e\u793a\u8be6\u7ec6\u4fe1\u606f", None))
        self.adb_devices_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u8c03\u8bd5\u8bbe\u5907\u5217\u8868", None))
        self.adb_start_server_pushButton.setText(QCoreApplication.translate("MainWindow", u"adb start-server", None))
        self.adb_kill_server_pushButton.setText(QCoreApplication.translate("MainWindow", u"adb kill-server", None))
        self.adb_reboot_pushButton.setText(QCoreApplication.translate("MainWindow", u"adb reboot", None))
        self.adb_reboot_bootloader_pushButton.setText(QCoreApplication.translate("MainWindow", u"adb reboot bootloader", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"Fastboot \u8bbe\u5907", None))
        self.fastboot_devices_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u5f15\u5bfc\u6a21\u5f0f\u8bbe\u5907\u5217\u8868", None))
        self.fastboot_reboot_pushButton.setText(QCoreApplication.translate("MainWindow", u"fastboot reboot", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u5e94\u7528\u5305\u540d", None))
        self.system_packages_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u7cfb\u7edf\u5e94\u7528", None))
        self.third_party_packages_checkBox.setText(QCoreApplication.translate("MainWindow", u"\u83b7\u53d6\u7b2c\u4e09\u65b9\u5e94\u7528", None))
        self.adb_shell_pm_list_packages_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u8be2\u5305\u540d", None))
        self.install_apk_pushButton.setText(QCoreApplication.translate("MainWindow", u"adb install <apk>", None))
        self.uninstall_apk_pushButton.setText(QCoreApplication.translate("MainWindow", u"adb uninstall <package>", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u8fdb\u7a0b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.adb_shell_am_force__stop_package_pushButton.setText(QCoreApplication.translate("MainWindow", u"adb shell am force-stop <package>", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.about_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.log_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u529f\u80fd\u533a", None))
        self.adb_pushButton.setText(QCoreApplication.translate("MainWindow", u"adb", None))
        self.frida_pushButton.setText(QCoreApplication.translate("MainWindow", u"frida", None))
    # retranslateUi

