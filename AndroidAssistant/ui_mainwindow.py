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
    QFrame, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QListWidget, QListWidgetItem,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QStackedWidget, QStatusBar,
    QTableWidget, QTableWidgetItem, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1183, 900)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_11 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
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
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, -100, 991, 1770))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.adb_devices_groupBox = QGroupBox(self.scrollAreaWidgetContents_5)
        self.adb_devices_groupBox.setObjectName(u"adb_devices_groupBox")
        self.verticalLayout_11 = QVBoxLayout(self.adb_devices_groupBox)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
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
        self.verticalLayout_10 = QVBoxLayout(self.frame_10)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.adb_devices_listWidget = QListWidget(self.frame_10)
        self.adb_devices_listWidget.setObjectName(u"adb_devices_listWidget")
        self.adb_devices_listWidget.setMinimumSize(QSize(0, 100))

        self.verticalLayout_10.addWidget(self.adb_devices_listWidget)

        self.frame_2 = QFrame(self.frame_10)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.adb_devices_l_checkBox = QCheckBox(self.frame_2)
        self.adb_devices_l_checkBox.setObjectName(u"adb_devices_l_checkBox")

        self.horizontalLayout.addWidget(self.adb_devices_l_checkBox)

        self.adb_devices_pushButton = QPushButton(self.frame_2)
        self.adb_devices_pushButton.setObjectName(u"adb_devices_pushButton")

        self.horizontalLayout.addWidget(self.adb_devices_pushButton)


        self.verticalLayout_10.addWidget(self.frame_2)


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

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.adb_reboot_pushButton = QPushButton(self.frame_8)
        self.adb_reboot_pushButton.setObjectName(u"adb_reboot_pushButton")

        self.horizontalLayout_7.addWidget(self.adb_reboot_pushButton)

        self.adb_reboot_recovery_pushButton = QPushButton(self.frame_8)
        self.adb_reboot_recovery_pushButton.setObjectName(u"adb_reboot_recovery_pushButton")

        self.horizontalLayout_7.addWidget(self.adb_reboot_recovery_pushButton)

        self.adb_reboot_bootloader_pushButton = QPushButton(self.frame_8)
        self.adb_reboot_bootloader_pushButton.setObjectName(u"adb_reboot_bootloader_pushButton")

        self.horizontalLayout_7.addWidget(self.adb_reboot_bootloader_pushButton)


        self.verticalLayout_16.addWidget(self.frame_8)

        self.frame_12 = QFrame(self.frame_5)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_12)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.frame_16 = QFrame(self.frame_12)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_16)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.adb_pc_label = QLabel(self.frame_17)
        self.adb_pc_label.setObjectName(u"adb_pc_label")

        self.horizontalLayout_8.addWidget(self.adb_pc_label)

        self.adb_pc_lineEdit = QLineEdit(self.frame_17)
        self.adb_pc_lineEdit.setObjectName(u"adb_pc_lineEdit")

        self.horizontalLayout_8.addWidget(self.adb_pc_lineEdit)

        self.adb_pc_pushButton = QPushButton(self.frame_17)
        self.adb_pc_pushButton.setObjectName(u"adb_pc_pushButton")

        self.horizontalLayout_8.addWidget(self.adb_pc_pushButton)


        self.verticalLayout_20.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_18)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.adb_mobile_label = QLabel(self.frame_18)
        self.adb_mobile_label.setObjectName(u"adb_mobile_label")

        self.horizontalLayout_12.addWidget(self.adb_mobile_label)

        self.adb_mobile_lineEdit = QLineEdit(self.frame_18)
        self.adb_mobile_lineEdit.setObjectName(u"adb_mobile_lineEdit")

        self.horizontalLayout_12.addWidget(self.adb_mobile_lineEdit)

        self.adb_mobile_pushButton = QPushButton(self.frame_18)
        self.adb_mobile_pushButton.setObjectName(u"adb_mobile_pushButton")

        self.horizontalLayout_12.addWidget(self.adb_mobile_pushButton)


        self.verticalLayout_20.addWidget(self.frame_18)

        self.adb_push_pc_mobile_pushButton = QPushButton(self.frame_16)
        self.adb_push_pc_mobile_pushButton.setObjectName(u"adb_push_pc_mobile_pushButton")

        self.verticalLayout_20.addWidget(self.adb_push_pc_mobile_pushButton)

        self.adb_pull_mobile_pc_pushButton = QPushButton(self.frame_16)
        self.adb_pull_mobile_pc_pushButton.setObjectName(u"adb_pull_mobile_pc_pushButton")

        self.verticalLayout_20.addWidget(self.adb_pull_mobile_pc_pushButton)


        self.verticalLayout_19.addWidget(self.frame_16)


        self.verticalLayout_16.addWidget(self.frame_12)


        self.verticalLayout_11.addWidget(self.frame_5)


        self.verticalLayout_12.addWidget(self.adb_devices_groupBox)

        self.line_3 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.line_3)

        self.fastboot_devices_groupBox = QGroupBox(self.scrollAreaWidgetContents_5)
        self.fastboot_devices_groupBox.setObjectName(u"fastboot_devices_groupBox")
        self.verticalLayout_17 = QVBoxLayout(self.fastboot_devices_groupBox)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_14 = QFrame(self.fastboot_devices_groupBox)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_14)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.fastboot_devices_listWidget = QListWidget(self.frame_14)
        self.fastboot_devices_listWidget.setObjectName(u"fastboot_devices_listWidget")
        self.fastboot_devices_listWidget.setMinimumSize(QSize(0, 100))

        self.verticalLayout_18.addWidget(self.fastboot_devices_listWidget)

        self.frame_15 = QFrame(self.frame_14)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.fastboot_devices_pushButton = QPushButton(self.frame_15)
        self.fastboot_devices_pushButton.setObjectName(u"fastboot_devices_pushButton")

        self.horizontalLayout_10.addWidget(self.fastboot_devices_pushButton)

        self.fastboot_getvar_all_pushButton = QPushButton(self.frame_15)
        self.fastboot_getvar_all_pushButton.setObjectName(u"fastboot_getvar_all_pushButton")

        self.horizontalLayout_10.addWidget(self.fastboot_getvar_all_pushButton)


        self.verticalLayout_18.addWidget(self.frame_15)


        self.verticalLayout_17.addWidget(self.frame_14)

        self.frame_13 = QFrame(self.fastboot_devices_groupBox)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.fastboot_reboot_pushButton = QPushButton(self.frame_13)
        self.fastboot_reboot_pushButton.setObjectName(u"fastboot_reboot_pushButton")

        self.horizontalLayout_9.addWidget(self.fastboot_reboot_pushButton)

        self.fastboot_reboot_recovery_pushButton = QPushButton(self.frame_13)
        self.fastboot_reboot_recovery_pushButton.setObjectName(u"fastboot_reboot_recovery_pushButton")

        self.horizontalLayout_9.addWidget(self.fastboot_reboot_recovery_pushButton)

        self.fastboot_reboot_bootloader_pushButton = QPushButton(self.frame_13)
        self.fastboot_reboot_bootloader_pushButton.setObjectName(u"fastboot_reboot_bootloader_pushButton")

        self.horizontalLayout_9.addWidget(self.fastboot_reboot_bootloader_pushButton)


        self.verticalLayout_17.addWidget(self.frame_13)

        self.flash_all_pushButton = QPushButton(self.fastboot_devices_groupBox)
        self.flash_all_pushButton.setObjectName(u"flash_all_pushButton")

        self.verticalLayout_17.addWidget(self.flash_all_pushButton)


        self.verticalLayout_12.addWidget(self.fastboot_devices_groupBox)

        self.line = QFrame(self.scrollAreaWidgetContents_5)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.line)

        self.package_groupBox = QGroupBox(self.scrollAreaWidgetContents_5)
        self.package_groupBox.setObjectName(u"package_groupBox")
        self.verticalLayout_14 = QVBoxLayout(self.package_groupBox)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.adb_shell_pm_list_packages_listWidget = QListWidget(self.package_groupBox)
        self.adb_shell_pm_list_packages_listWidget.setObjectName(u"adb_shell_pm_list_packages_listWidget")
        self.adb_shell_pm_list_packages_listWidget.setMinimumSize(QSize(0, 200))
        self.adb_shell_pm_list_packages_listWidget.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)

        self.verticalLayout_14.addWidget(self.adb_shell_pm_list_packages_listWidget)

        self.frame_6 = QFrame(self.package_groupBox)
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
        self.adb_shell_pm_list_packages_s_checkBox = QCheckBox(self.frame_9)
        self.adb_shell_pm_list_packages_s_checkBox.setObjectName(u"adb_shell_pm_list_packages_s_checkBox")

        self.verticalLayout_5.addWidget(self.adb_shell_pm_list_packages_s_checkBox)

        self.adb_shell_pm_list_packages_3_checkBox = QCheckBox(self.frame_9)
        self.adb_shell_pm_list_packages_3_checkBox.setObjectName(u"adb_shell_pm_list_packages_3_checkBox")

        self.verticalLayout_5.addWidget(self.adb_shell_pm_list_packages_3_checkBox)


        self.horizontalLayout_5.addWidget(self.frame_9)

        self.adb_shell_pm_list_packages_pushButton = QPushButton(self.frame_6)
        self.adb_shell_pm_list_packages_pushButton.setObjectName(u"adb_shell_pm_list_packages_pushButton")

        self.horizontalLayout_5.addWidget(self.adb_shell_pm_list_packages_pushButton)


        self.verticalLayout_14.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.package_groupBox)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.adb_install_apk_pushButton = QPushButton(self.frame_7)
        self.adb_install_apk_pushButton.setObjectName(u"adb_install_apk_pushButton")

        self.horizontalLayout_6.addWidget(self.adb_install_apk_pushButton)

        self.adb_uninstall_package_pushButton = QPushButton(self.frame_7)
        self.adb_uninstall_package_pushButton.setObjectName(u"adb_uninstall_package_pushButton")

        self.horizontalLayout_6.addWidget(self.adb_uninstall_package_pushButton)


        self.verticalLayout_14.addWidget(self.frame_7)

        self.adb_shell_am_force__stop_package_pushButton = QPushButton(self.package_groupBox)
        self.adb_shell_am_force__stop_package_pushButton.setObjectName(u"adb_shell_am_force__stop_package_pushButton")

        self.verticalLayout_14.addWidget(self.adb_shell_am_force__stop_package_pushButton)


        self.verticalLayout_12.addWidget(self.package_groupBox)

        self.line_2 = QFrame(self.scrollAreaWidgetContents_5)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_12.addWidget(self.line_2)

        self.process_groupBox = QGroupBox(self.scrollAreaWidgetContents_5)
        self.process_groupBox.setObjectName(u"process_groupBox")
        self.verticalLayout_15 = QVBoxLayout(self.process_groupBox)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.process_tableWidget = QTableWidget(self.process_groupBox)
        self.process_tableWidget.setObjectName(u"process_tableWidget")
        self.process_tableWidget.setMinimumSize(QSize(0, 400))

        self.verticalLayout_15.addWidget(self.process_tableWidget)

        self.frame = QFrame(self.process_groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.keyword_label = QLabel(self.frame)
        self.keyword_label.setObjectName(u"keyword_label")

        self.horizontalLayout_2.addWidget(self.keyword_label)

        self.process_keyword_lineEdit = QLineEdit(self.frame)
        self.process_keyword_lineEdit.setObjectName(u"process_keyword_lineEdit")

        self.horizontalLayout_2.addWidget(self.process_keyword_lineEdit)

        self.process_search_pushButton = QPushButton(self.frame)
        self.process_search_pushButton.setObjectName(u"process_search_pushButton")

        self.horizontalLayout_2.addWidget(self.process_search_pushButton)


        self.verticalLayout_15.addWidget(self.frame)


        self.verticalLayout_12.addWidget(self.process_groupBox)

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
        self.tool_page = QWidget()
        self.tool_page.setObjectName(u"tool_page")
        self.verticalLayout_4 = QVBoxLayout(self.tool_page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.rename_apk_pushButton = QPushButton(self.tool_page)
        self.rename_apk_pushButton.setObjectName(u"rename_apk_pushButton")

        self.verticalLayout_4.addWidget(self.rename_apk_pushButton)

        self.stackedWidget.addWidget(self.tool_page)

        self.horizontalLayout_11.addWidget(self.stackedWidget)

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

        self.tool_pushButton = QPushButton(self.groupBox_6)
        self.tool_pushButton.setObjectName(u"tool_pushButton")

        self.verticalLayout_7.addWidget(self.tool_pushButton)


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
        self.adb_devices_l_checkBox.setText(QCoreApplication.translate("MainWindow", u"-l \uff08\u663e\u793a\u8be6\u7ec6\u4fe1\u606f\uff09", None))
        self.adb_devices_pushButton.setText(QCoreApplication.translate("MainWindow", u"adb devices", None))
        self.adb_start_server_pushButton.setText(QCoreApplication.translate("MainWindow", u"adb start-server", None))
        self.adb_kill_server_pushButton.setText(QCoreApplication.translate("MainWindow", u"adb kill-server", None))
        self.adb_reboot_pushButton.setText(QCoreApplication.translate("MainWindow", u"adb reboot", None))
        self.adb_reboot_recovery_pushButton.setText(QCoreApplication.translate("MainWindow", u"adb reboot recovery", None))
        self.adb_reboot_bootloader_pushButton.setText(QCoreApplication.translate("MainWindow", u"adb reboot bootloader", None))
        self.adb_pc_label.setText(QCoreApplication.translate("MainWindow", u"pc       ", None))
        self.adb_pc_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
        self.adb_mobile_label.setText(QCoreApplication.translate("MainWindow", u"mobile", None))
        self.adb_mobile_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6d4f\u89c8", None))
        self.adb_push_pc_mobile_pushButton.setText(QCoreApplication.translate("MainWindow", u"adb push <pc> <mobile>", None))
        self.adb_pull_mobile_pc_pushButton.setText(QCoreApplication.translate("MainWindow", u"adb pull <mobile> <pc>", None))
        self.fastboot_devices_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Fastboot \u8bbe\u5907", None))
        self.fastboot_devices_pushButton.setText(QCoreApplication.translate("MainWindow", u"fastboot devices", None))
        self.fastboot_getvar_all_pushButton.setText(QCoreApplication.translate("MainWindow", u"fastboot getvar all", None))
        self.fastboot_reboot_pushButton.setText(QCoreApplication.translate("MainWindow", u"fastboot reboot", None))
        self.fastboot_reboot_recovery_pushButton.setText(QCoreApplication.translate("MainWindow", u"fastboot reboot recovery", None))
        self.fastboot_reboot_bootloader_pushButton.setText(QCoreApplication.translate("MainWindow", u"fastboot reboot bootloader", None))
        self.flash_all_pushButton.setText(QCoreApplication.translate("MainWindow", u"flash-all", None))
        self.package_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Package \u5305\u540d", None))
        self.adb_shell_pm_list_packages_s_checkBox.setText(QCoreApplication.translate("MainWindow", u"-s \uff08\u83b7\u53d6\u7cfb\u7edf\u5e94\u7528\uff09", None))
        self.adb_shell_pm_list_packages_3_checkBox.setText(QCoreApplication.translate("MainWindow", u"-3 \uff08\u83b7\u53d6\u7b2c\u4e09\u65b9\u5e94\u7528\uff09", None))
        self.adb_shell_pm_list_packages_pushButton.setText(QCoreApplication.translate("MainWindow", u"adb shell pm list packages", None))
        self.adb_install_apk_pushButton.setText(QCoreApplication.translate("MainWindow", u"adb install <apk>", None))
        self.adb_uninstall_package_pushButton.setText(QCoreApplication.translate("MainWindow", u"adb uninstall <package>", None))
        self.adb_shell_am_force__stop_package_pushButton.setText(QCoreApplication.translate("MainWindow", u"adb shell am force-stop <package>", None))
        self.process_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Process \u8fdb\u7a0b", None))
        self.keyword_label.setText(QCoreApplication.translate("MainWindow", u"\u5173\u952e\u8bcd", None))
        self.process_search_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.rename_apk_pushButton.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u547d\u540dapk", None))
        self.about_menu.setTitle(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
        self.log_groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u65e5\u5fd7", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u529f\u80fd\u533a", None))
        self.adb_pushButton.setText(QCoreApplication.translate("MainWindow", u"adb", None))
        self.frida_pushButton.setText(QCoreApplication.translate("MainWindow", u"frida", None))
        self.tool_pushButton.setText(QCoreApplication.translate("MainWindow", u"tool", None))
    # retranslateUi

