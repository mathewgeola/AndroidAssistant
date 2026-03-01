import os
import re
import sys

import pandas as pd
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QMenu, QTableWidgetItem, \
    QAbstractItemView, QDialog, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QPushButton, QTextBrowser
from androguard.core import apk as androguard_core_apk

from cmd import Cmd
from logger import Logger
from signals import Signals
from ui_mainwindow import Ui_MainWindow
import sys
import os
import subprocess
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QPushButton, QLineEdit, QDialog,
    QTreeWidget, QTreeWidgetItem,
    QHBoxLayout, QLabel, QFrame
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QStyle


class BaseFileDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.resize(800, 650)
        self.setMinimumSize(700, 500)

        self.current_path = self.get_root_path()
        self.history = []
        self.future = []
        self.only_dir_mode = False

        main_layout = QVBoxLayout(self)
        main_layout.setSpacing(8)

        self.title_label = QLabel("文件浏览器")
        self.title_label.setStyleSheet("font-size:16px;font-weight:bold;")
        main_layout.addWidget(self.title_label)

        nav_layout = QHBoxLayout()
        self.back_btn = QPushButton("←")
        self.forward_btn = QPushButton("→")

        self.path_edit = QLineEdit()
        self.path_edit.returnPressed.connect(self.jump_to_path)

        nav_layout.addWidget(self.back_btn)
        nav_layout.addWidget(self.forward_btn)
        nav_layout.addWidget(self.path_edit)
        main_layout.addLayout(nav_layout)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Sunken)
        main_layout.addWidget(line)

        self.tree = QTreeWidget()
        self.tree.setHeaderLabels(["名称"])
        self.tree.setColumnWidth(0, 600)
        self.tree.setSelectionMode(QTreeWidget.ExtendedSelection)
        self.tree.setAlternatingRowColors(True)
        main_layout.addWidget(self.tree, stretch=1)

        self.selected_label = QLineEdit()
        self.selected_label.setReadOnly(True)
        self.selected_label.setPlaceholderText("已选择路径（支持多选）")
        main_layout.addWidget(self.selected_label)

        bottom_layout = QHBoxLayout()
        bottom_layout.addStretch()
        self.ok_btn = QPushButton("确定")
        self.cancel_btn = QPushButton("取消")
        self.ok_btn.setMinimumWidth(100)
        self.cancel_btn.setMinimumWidth(100)
        bottom_layout.addWidget(self.ok_btn)
        bottom_layout.addWidget(self.cancel_btn)
        main_layout.addLayout(bottom_layout)

        self.tree.itemDoubleClicked.connect(self.enter_directory)
        self.tree.itemSelectionChanged.connect(self.update_selected_label)
        self.back_btn.clicked.connect(self.go_back)
        self.forward_btn.clicked.connect(self.go_forward)
        self.ok_btn.clicked.connect(self.accept)
        self.cancel_btn.clicked.connect(self.reject)

        self.load_files()

    def add_item(self, name, is_dir):
        icon = self.style().standardIcon(
            QStyle.SP_DirIcon if is_dir else QStyle.SP_FileIcon
        )
        display_name = name + "/" if is_dir else name

        item = QTreeWidgetItem([display_name])
        item.setIcon(0, icon)
        item.setData(0, Qt.UserRole, is_dir)
        self.tree.addTopLevelItem(item)

    def jump_to_path(self):
        new_path = self.path_edit.text().strip()
        if not new_path:
            return
        self.history.append(self.current_path)
        self.current_path = new_path
        self.load_files()

    def load_files(self):
        self.tree.clear()
        self.path_edit.setText(self.current_path)
        self.title_label.setText(f"选择的目录或文件: {self.current_path}")

        parent = self.parent_path(self.current_path)
        if parent and parent != self.current_path:
            parent_item = QTreeWidgetItem([".."])
            parent_item.setIcon(0, self.style().standardIcon(QStyle.SP_ArrowUp))
            parent_item.setData(0, Qt.UserRole, "parent")
            self.tree.addTopLevelItem(parent_item)

        dirs, files = self.list_dir(self.current_path)
        dirs.sort()
        files.sort()

        for d in dirs:
            self.add_item(d, True)

        if not self.only_dir_mode:
            for f in files:
                self.add_item(f, False)

        self.update_selected_label()
        self.update_nav_buttons()

    def enter_directory(self, item):
        data = item.data(0, Qt.UserRole)

        if data == "parent":
            self.future.clear()
            self.history.append(self.current_path)
            self.current_path = self.parent_path(self.current_path)

        elif data:
            self.history.append(self.current_path)
            self.future.clear()
            name = item.text(0).rstrip("/")
            self.current_path = self.join_path(self.current_path, name)

        self.load_files()

    def update_selected_label(self):
        items = self.tree.selectedItems()
        paths = []

        for item in items:
            data = item.data(0, Qt.UserRole)
            if data == "parent":
                continue

            name = item.text(0).rstrip("/")
            full = self.join_path(self.current_path, name)

            if self.only_dir_mode and not data:
                continue

            paths.append(full)

        self.selected_label.setText(";".join(paths))

    def selected_files(self):
        return self.selected_label.text().split(";") if self.selected_label.text() else []

    def go_back(self):
        if not self.history:
            return
        self.future.append(self.current_path)
        self.current_path = self.history.pop()
        self.load_files()

    def go_forward(self):
        if not self.future:
            return
        self.history.append(self.current_path)
        self.current_path = self.future.pop()
        self.load_files()

    def update_nav_buttons(self):
        self.back_btn.setEnabled(bool(self.history))
        self.forward_btn.setEnabled(bool(self.future))

    def get_root_path(self):
        raise NotImplementedError

    def list_dir(self, path):
        raise NotImplementedError

    def join_path(self, base, name):
        raise NotImplementedError

    def parent_path(self, path):
        raise NotImplementedError

    @classmethod
    def getOpenFileNames(cls, parent=None):
        dialog = cls(parent)
        dialog.only_dir_mode = False
        dialog.tree.setSelectionMode(QTreeWidget.ExtendedSelection)
        dialog.setWindowTitle("选择文件或目录")

        if dialog.exec():
            return dialog.selected_files()
        return []

    @classmethod
    def getExistingDirectory(cls, parent=None):
        dialog = cls(parent)
        dialog.only_dir_mode = True
        dialog.tree.setSelectionMode(QTreeWidget.SingleSelection)
        dialog.setWindowTitle("选择目录")

        if dialog.exec():
            return dialog.selected_files()[0]
        return []


class PcFileDialog(BaseFileDialog):

    def get_root_path(self):
        return os.path.abspath(os.sep)

    def list_dir(self, path):
        try:
            entries = os.listdir(path)
        except:  # noqa
            return [], []

        dirs, files = [], []
        for name in entries:
            full = os.path.join(path, name)
            if os.path.isdir(full):
                dirs.append(name)
            else:
                files.append(name)
        return dirs, files

    def join_path(self, base, name):
        return os.path.join(base, name)

    def parent_path(self, path):
        return os.path.dirname(path.rstrip(os.sep))


class MobileFileDialog(BaseFileDialog):

    def get_root_path(self):
        return "/"

    def list_dir(self, path):
        cmd = ["adb", "shell", "su", "-c", "ls", "-l", path]
        result = subprocess.run(cmd, capture_output=True, text=True)

        dirs, files = [], []
        for line in result.stdout.splitlines():
            parts = line.split()
            if len(parts) < 6:
                continue
            name = parts[-1]
            if line.startswith("d"):
                dirs.append(name)
            else:
                files.append(name)
        return dirs, files

    def join_path(self, base, name):
        return base.rstrip("/") + "/" + name

    def parent_path(self, path):
        return "/".join(path.rstrip("/").split("/")[:-1])


class ADBPushPullDialog(QDialog):
    def __init__(self, title, parent=None):
        super().__init__(parent)
        self.title = title
        self.setWindowTitle(self.title)
        self.resize(450, 200)

        main_layout = QVBoxLayout(self)

        row1 = QHBoxLayout()
        if self.title == "adb push":
            self.label1 = QLabel("pc       ：")
        else:
            assert self.title == "adb pull"
            self.label1 = QLabel("mobile：")
        self.line_edit1 = QLineEdit()
        self.line_edit1.setReadOnly(True)
        self.btn1 = QPushButton("浏览")
        row1.addWidget(self.label1)
        row1.addWidget(self.line_edit1)
        row1.addWidget(self.btn1)
        main_layout.addLayout(row1)

        row2 = QHBoxLayout()
        if self.title == "adb push":
            self.label2 = QLabel("mobile：")
        else:
            assert self.title == "adb pull"
            self.label2 = QLabel("pc       ：")
        self.line_edit2 = QLineEdit()
        self.line_edit2.setReadOnly(True)
        self.btn2 = QPushButton("浏览")
        row2.addWidget(self.label2)
        row2.addWidget(self.line_edit2)
        row2.addWidget(self.btn2)
        main_layout.addLayout(row2)

        self.text_browser = QTextBrowser()
        main_layout.addWidget(self.text_browser)

        bottom_layout = QHBoxLayout()
        bottom_layout.addStretch()
        self.ok_btn = QPushButton("确定")
        self.cancel_btn = QPushButton("取消")
        bottom_layout.addWidget(self.ok_btn)
        bottom_layout.addWidget(self.cancel_btn)
        main_layout.addLayout(bottom_layout)

        self.ok_btn.clicked.connect(self.on_ok)
        self.cancel_btn.clicked.connect(self.close)

        def on_btn1_clicked():
            if title == "adb push":
                value = ";".join(PcFileDialog.getOpenFileNames(self))

            else:
                assert title == "adb pull"
                value = ";".join(MobileFileDialog.getOpenFileNames(self))
            self.update_line(self.line_edit1, value)

        def on_btn2_clicked():
            if title == "adb push":
                value = MobileFileDialog.getExistingDirectory(self)
            else:
                assert title == "adb pull"
                value = PcFileDialog.getExistingDirectory(self)
            self.update_line(self.line_edit2, value)

        self.btn1.clicked.connect(on_btn1_clicked)
        self.btn2.clicked.connect(on_btn2_clicked)

        self.line_edit1.textChanged.connect(self.update_display)
        self.line_edit2.textChanged.connect(self.update_display)

    def update_line(self, line_edit, value):
        line_edit.setText(value)

    def update_display(self):
        text1 = self.line_edit1.text()
        text2 = self.line_edit2.text()

        self.text_browser.clear()

        for i in text1.split(";"):
            self.text_browser.append(f"{self.title} {i} {text2}")

    def on_ok(self):
        print(self.line_edit.text())
        self.close()


class AndroidAssistant(QMainWindow):
    BASE_DIR = os.path.dirname(__file__)
    RESOURCES_DIR = os.path.join(BASE_DIR, "resources")
    APKS_DIR = os.path.join(RESOURCES_DIR, "apks")
    ICON_PATH = os.path.join(RESOURCES_DIR, "app.ico")

    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon(self.ICON_PATH))
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self)

        self._init()
        self._init_signal()

    def _init(self):
        self._ui.adb_pushButton.clicked.connect(
            lambda: self._ui.stackedWidget.setCurrentWidget(self._ui.adb_page)
        )
        self._ui.frida_pushButton.clicked.connect(
            lambda: self._ui.stackedWidget.setCurrentWidget(self._ui.frida_page)
        )
        self._ui.tool_pushButton.clicked.connect(
            lambda: self._ui.stackedWidget.setCurrentWidget(self._ui.tool_page)
        )

        self._ui.adb_start_server_pushButton.clicked.connect(
            lambda: self._cmd.run("adb", ["start-server"])
        )
        self._ui.adb_kill_server_pushButton.clicked.connect(
            lambda: self._cmd.run("adb", ["kill-server"])
        )

        self._ui.adb_reboot_pushButton.clicked.connect(
            lambda: self._cmd.run("adb", ["reboot"])
        )
        self._ui.adb_reboot_recovery_pushButton.clicked.connect(
            lambda: self._cmd.run("adb", ["reboot", "recovery"])
        )
        self._ui.adb_reboot_bootloader_pushButton.clicked.connect(
            lambda: self._cmd.run("adb", ["reboot", "bootloader"])
        )

        self._ui.process_search_pushButton.clicked.connect(self.on_process_search_pushButton_clicked)

        self._ui.adb_devices_pushButton.clicked.connect(self.on_adb_devices_pushButton_clicked)

        self._ui.rename_apk_pushButton.clicked.connect(self.on_rename_apk_pushButton_clicked)

        self._ui.adb_shell_pm_list_packages_pushButton.clicked.connect(
            self.on_adb_shell_pm_list_packages_pushButton_clicked
        )
        self._ui.adb_reboot_bootloader_pushButton.clicked.connect(
            lambda: self._cmd.run("adb", ["reboot", "bootloader"])
        )
        self._ui.fastboot_reboot_pushButton.clicked.connect(
            lambda: self._cmd.run("fastboot", ["reboot"])
        )
        self._ui.fastboot_devices_pushButton.clicked.connect(self.on_fastboot_devices_pushButton_clicked)

        # def on_adb_push_pc_mobile_pushButton_clicked():
        #     pc_file_path = self._ui.pc_lineEdit.text()
        #     mobile_file_path = self._ui.mobile_lineEdit.text()
        #     if not pc_file_path or not mobile_file_path:
        #         return
        #     program_args = ["push", pc_file_path, mobile_file_path]
        #     self._cmd.run("adb", program_args)

        def on_adb_push_pc_mobile_pushButton_clicked():
            dialog = ADBPushPullDialog("adb push", self)
            dialog.show()

        self._ui.adb_push_pc_mobile_pushButton.clicked.connect(on_adb_push_pc_mobile_pushButton_clicked)

        # def on_adb_pull_mobile_pc_pushButton_clicked():
        #     mobile_file_path = self._ui.mobile_lineEdit.text()
        #     pc_file_path = self._ui.pc_lineEdit.text()
        #     if not mobile_file_path or not pc_file_path:
        #         return
        #     program_args = ["pull", mobile_file_path, pc_file_path]
        #     self._cmd.run("adb", program_args)

        def on_adb_pull_mobile_pc_pushButton_clicked():
            dialog = ADBPushPullDialog("adb pull", self)
            dialog.show()

        self._ui.adb_pull_mobile_pc_pushButton.clicked.connect(on_adb_pull_mobile_pc_pushButton_clicked)

        def on_fastboot_flash_boot_img_pushButton_clicked():
            img_file_path, _ = QFileDialog.getOpenFileName(
                self,
                "单选要刷入的 img 文件路径",
                self.APKS_DIR,
                "img 文件路径 (*.img)"
            )

            if img_file_path:
                self._cmd.run("fastboot", ["flash", "boot", img_file_path])

        self._ui.fastboot_flash_boot_img_pushButton.clicked.connect(on_fastboot_flash_boot_img_pushButton_clicked)

        def on_fastboot_getvar_all_pushButton_clicked():
            def callback(code, output):
                self._ui.fastboot_devices_listWidget.clear()
                if code == 0:
                    data = output.replace("\r\n", "\n")
                    items = re.findall(r"\(bootloader\) (.*?)\n", data, re.DOTALL)
                    self._ui.fastboot_devices_listWidget.addItems(items)

            self._cmd.run("fastboot", ["getvar", "all"], callback)

        self._ui.fastboot_getvar_all_pushButton.clicked.connect(on_fastboot_getvar_all_pushButton_clicked)

        self._ui.adb_install_apk_pushButton.clicked.connect(self.on_adb_install_apk_pushButton_clicked)
        self._ui.adb_uninstall_package_pushButton.clicked.connect(self.on_adb_uninstall_package_pushButton_clicked)
        self._ui.adb_shell_am_force__stop_package_pushButton.clicked.connect(
            self.on_adb_shell_am_force__stop_package_pushButton_clicked
        )

        self._ui.log_textBrowser.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        self._ui.log_textBrowser.customContextMenuRequested.connect(self.context_menu)

        # log_file_path = "app.log"
        log_file_path = None
        self._logger = Logger(self._ui.log_textBrowser, log_file_path)

        self._cmd = Cmd(self._logger)

    def _init_signal(self):
        self._signals = Signals()
        self._signals.adb_shell_pm_list_packages.connect(
            self.on_adb_shell_pm_list_packages_pushButton_clicked
        )

    def context_menu(self, point):
        menu = QMenu()
        clear_action = menu.addAction("清空")
        action = menu.exec(self._ui.log_textBrowser.mapToGlobal(point))
        if action == clear_action:
            self._ui.log_textBrowser.clear()

    @property
    def ui(self):
        return self._ui

    @property
    def logger(self):
        return self._logger

    def on_adb_shell_pm_list_packages_pushButton_clicked(self):
        def callback(code, output):
            self._ui.adb_shell_pm_list_packages_listWidget.clear()
            if code == 0:
                items = [line.replace("package:", "").strip() for line in output.strip().split("\n") if line.strip()]
                self._ui.adb_shell_pm_list_packages_listWidget.addItems(items)

        program_args = ["shell", "pm", "list", "packages"]
        if self._ui.adb_shell_pm_list_packages_s_checkBox.isChecked():
            program_args.append("-s")
        if self._ui.adb_shell_pm_list_packages_3_checkBox.isChecked():
            program_args.append("-3")
        self._cmd.run("adb", program_args, callback)

    def on_process_search_pushButton_clicked(self):
        def callback(code, output, process_keyword):
            try:
                self._ui.process_tableWidget.clear()
                self._ui.process_tableWidget.setShowGrid(True)
                self._ui.process_tableWidget.horizontalHeader().setVisible(True)
                self._ui.process_tableWidget.verticalHeader().setVisible(True)

                if code == 0:
                    data = [line.split() for line in output.replace("\r\n", "\n").strip().split("\n")]
                    columns = data.pop(0)
                    df = pd.DataFrame(data, columns=columns)

                    if process_keyword:
                        df = df[df["NAME"].str.contains(process_keyword)]

                    self._ui.process_tableWidget.setRowCount(len(df))
                    self._ui.process_tableWidget.setColumnCount(len(df.columns))
                    self._ui.process_tableWidget.setHorizontalHeaderLabels(df.columns)
                    self._ui.process_tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)

                    for row_idx in range(len(df)):
                        for col_idx in range(len(df.columns)):
                            value = df.iat[row_idx, col_idx]
                            widget_item = QTableWidgetItem(str(value))
                            widget_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                            self._ui.process_tableWidget.setItem(row_idx, col_idx, widget_item)

            except Exception:  # noqa
                self._ui.process_tableWidget.clear()
                self._ui.process_tableWidget.setShowGrid(False)
                self._ui.process_tableWidget.horizontalHeader().setVisible(False)
                self._ui.process_tableWidget.verticalHeader().setVisible(False)
                QMessageBox.warning(self, "错误", "进程搜索失败")

        def main():
            program_args = ["shell", "sh", "-c", "ps | grep -v grep"]
            text = self._ui.process_keyword_lineEdit.text()
            process_keyword = text.strip()
            self._cmd.run("adb", program_args, callback, callback_kwargs=dict(process_keyword=process_keyword))

        main()

    def on_rename_apk_pushButton_clicked(self):
        androguard_core_apk.logger.remove(handler_id=None)

        apk_file_paths, _ = QFileDialog.getOpenFileNames(
            self,
            "可多选要重命名的 apk 文件路径",
            self.APKS_DIR,
            "apk 文件路径 (*.apk)"
        )

        if apk_file_paths:
            for apk_file_path in apk_file_paths:
                self._logger.debug(f"{apk_file_path}")
                apk_file_path = os.path.abspath(apk_file_path)
                dir_path = os.path.dirname(apk_file_path)
                apk = androguard_core_apk.APK(apk_file_path)
                new_apk_file_name = apk.get_app_name() + "_" + apk.get_androidversion_name() + ".apk"
                new_apk_file_path = os.path.abspath(os.path.join(dir_path, new_apk_file_name))
                if apk_file_path != new_apk_file_path:
                    if os.path.exists(new_apk_file_path):
                        os.remove(new_apk_file_path)
                    os.rename(apk_file_path, new_apk_file_path)
                    self._logger.success(f"{apk_file_path} -> {new_apk_file_path}")

    def on_adb_devices_pushButton_clicked(self):
        def callback(code, output):
            self._ui.adb_devices_listWidget.clear()
            if code == 0:
                data = re.findall(r"List of devices attached(.*)", output, re.DOTALL)[0].strip()
                data = data.replace("\r\n", "").split("\n")
                items = ["\t".join(i.split()) for i in data]

                self._ui.adb_devices_listWidget.addItems(items)

        program_args = ["devices"]
        if self._ui.adb_devices_l_checkBox.isChecked():
            program_args.append("-l")
        self._cmd.run("adb", program_args, callback)

    def on_fastboot_devices_pushButton_clicked(self):
        def callback(code, output):
            self._ui.fastboot_devices_listWidget.clear()
            if code == 0:
                if output:
                    data = output.strip()
                    items = data.split("\r\n")
                    if len(items) == 1:
                        items = items[0].split("\n")
                    self._ui.fastboot_devices_listWidget.addItems(items)

        program_args = ["devices"]
        self._cmd.run("fastboot", program_args, callback)

    def on_adb_install_apk_pushButton_clicked(self):
        apk_file_paths, _ = QFileDialog.getOpenFileNames(
            self,
            "可多选要安装的 apk 文件路径",
            self.APKS_DIR,
            "apk 文件路径 (*.apk)"
        )

        if apk_file_paths:
            total = len(apk_file_paths)
            finished_count = 0
            success_dict = {}
            fail_dict = {}

            def callback(code, output, apk_file_path):
                nonlocal finished_count

                finished_count += 1

                if code == 0:
                    success_dict[apk_file_path] = output
                else:
                    fail_dict[apk_file_path] = output

                if finished_count == total:
                    success_count = len(success_dict)
                    fail_count = len(fail_dict)

                    result_msg = (
                        f"共安装 {total} 个应用\n"
                        f"成功 {success_count} 个\n"
                        f"失败 {fail_count} 个\n\n"
                    )

                    if success_dict:
                        result_msg += "安装成功的 apk 文件路径：\n"
                        result_msg += "\n".join(list(success_dict.keys()))
                        result_msg += "\n\n"

                    if fail_dict:
                        result_msg += "安装失败的 apk 文件路径和安装输出：\n"
                        for k, v in fail_dict.items():
                            result_msg += f"apk 文件路径：{k}\n安装输出：{v}\n\n"

                    QMessageBox.information(self, "安装结果", result_msg)

                self._signals.adb_shell_pm_list_packages.emit()

            def main():
                for apk_file_path in apk_file_paths:
                    self._cmd.run(
                        "adb", ["install", apk_file_path],
                        callback, callback_kwargs=dict(apk_file_path=apk_file_path)
                    )

            main()

    def on_adb_uninstall_package_pushButton_clicked(self):
        items = self._ui.adb_shell_pm_list_packages_listWidget.selectedItems()
        if not items:
            return

        package_names = [item.text() for item in items]

        reply = QMessageBox.question(
            self,
            "提示",
            f"确定卸载：\n{'，'.join(package_names)} ?"
        )
        if reply == QMessageBox.StandardButton.Yes:
            total = len(package_names)
            finished_count = 0
            success_dict = {}
            fail_dict = {}

            def callback(code, output, package_name):
                nonlocal finished_count

                finished_count += 1

                if code == 0:
                    success_dict[package_name] = output
                else:
                    fail_dict[package_name] = output

                if finished_count == total:
                    success_count = len(success_dict)
                    fail_count = len(fail_dict)

                    result_msg = (
                        f"共卸载 {total} 个应用\n"
                        f"成功 {success_count} 个\n"
                        f"失败 {fail_count} 个\n\n"
                    )

                    if success_dict:
                        result_msg += "卸载成功的应用包名：\n"
                        result_msg += "\n".join(list(success_dict.keys()))
                        result_msg += "\n\n"

                    if fail_dict:
                        result_msg += "卸载失败的应用包名和卸载输出：\n"
                        for k, v in fail_dict.items():
                            result_msg += f"应用包名：{k}\n卸载输出：{v}\n\n"

                    QMessageBox.information(self, "卸载结果", result_msg)

                self._signals.adb_shell_pm_list_packages.emit()

            def main():
                for package_name in package_names:
                    self._cmd.run(
                        "adb", ["uninstall", package_name],
                        callback, callback_kwargs=dict(package_name=package_name)
                    )

            main()

    def on_adb_shell_am_force__stop_package_pushButton_clicked(self):
        selected_items = self._ui.adb_shell_pm_list_packages_listWidget.selectedItems()
        if not selected_items:
            return

        package_names = [i.text() for i in selected_items]
        reply = QMessageBox.question(
            self,
            "提示",
            f"确定强制停止：\n{'，'.join(package_names)} ?"
        )
        if reply == QMessageBox.StandardButton.Yes:
            total = len(package_names)
            finished_count = 0
            success_dict = {}
            fail_dict = {}

            def callback(code, output, package_name):
                nonlocal finished_count

                finished_count += 1

                if code == 0:
                    success_dict[package_name] = output
                else:
                    fail_dict[package_name] = output

                if finished_count == total:
                    success_count = len(success_dict)
                    fail_count = len(fail_dict)

                    result_msg = (
                        f"共强制停止 {total} 个应用\n"
                        f"成功 {success_count} 个\n"
                        f"失败 {fail_count} 个\n\n"
                    )

                    if success_dict:
                        result_msg += "强制停止的应用包名：\n"
                        result_msg += "\n".join(list(success_dict.keys()))
                        result_msg += "\n\n"

                    if fail_dict:
                        result_msg += "强制停止的应用包名和输出：\n"
                        for k, v in fail_dict.items():
                            result_msg += f"应用包名：{k}\n输出：{v}\n\n"

                    QMessageBox.information(self, "强制停止结果", result_msg)

                self._signals.adb_shell_pm_list_packages.emit()

            def main():
                for package_name in package_names:
                    self._cmd.run(
                        "adb", ["shell", "am", "force-stop", package_name],
                        callback, callback_kwargs=dict(package_name=package_name)
                    )

            main()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    aa = AndroidAssistant()
    aa.show()
    sys.exit(app.exec())
