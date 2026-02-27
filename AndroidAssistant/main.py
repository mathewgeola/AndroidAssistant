import os
import re
import sys

from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QMenu

from cmd import Cmd
from logger import Logger
from signals import Signals
from ui_mainwindow import Ui_MainWindow


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

        self._ui.adb_kill_server_pushButton.clicked.connect(self.on_adb_kill_server_pushButton_clicked)
        self._ui.adb_start_server_pushButton.clicked.connect(self.on_adb_start_server_pushButton_clicked)
        self._ui.adb_devices_pushButton.clicked.connect(self.on_adb_devices_pushButton_clicked)

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

        self._ui.install_apk_pushButton.clicked.connect(self.on_install_apk_pushButton_clicked)
        self._ui.uninstall_apk_pushButton.clicked.connect(self.on_uninstall_apk_pushButton_clicked)
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

    def on_adb_kill_server_pushButton_clicked(self):
        self._cmd.run("adb", ["kill-server"])

    def on_adb_start_server_pushButton_clicked(self):
        self._cmd.run("adb", ["start-server"])

    def on_adb_shell_pm_list_packages_pushButton_clicked(self):
        def callback(code, output):
            self._ui.adb_shell_pm_list_packages_listWidget.clear()
            if code == 0:
                items = [line.replace("package:", "").strip() for line in output.strip().split("\n") if line.strip()]
                self._ui.adb_shell_pm_list_packages_listWidget.addItems(items)

        program_args = ["shell", "pm", "list", "packages"]
        if self._ui.system_packages_checkBox.isChecked():
            program_args.append("-s")
        if self._ui.third_party_packages_checkBox.isChecked():
            program_args.append("-3")
        self._cmd.run("adb", program_args, callback)

    def on_adb_devices_pushButton_clicked(self):
        def callback(code, output):
            self._ui.adb_devices_listWidget.clear()
            if code == 0:
                data = re.findall(r"List of devices attached(.*)", output, re.DOTALL)[0].strip()
                items = data.split("\r\n")
                if len(items) == 1:
                    items = items[0].split("\n")

                self._ui.adb_devices_listWidget.addItems(items)

        program_args = ["devices"]
        if self._ui.long_checkBox.isChecked():
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

    def on_install_apk_pushButton_clicked(self):
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

    def on_uninstall_apk_pushButton_clicked(self):
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
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    aa = AndroidAssistant()
    aa.show()
    sys.exit(app.exec())
