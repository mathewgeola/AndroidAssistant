import os
import sys

from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QPushButton, QDialog, QVBoxLayout, QListWidget, \
    QMessageBox, QMenu

from cmd import Cmd
from logger import Logger
from ui_mainwindow import Ui_MainWindow


class PackageNamesDialog(QDialog):
    update_list_signal = Signal(list)

    def __init__(self, cmd: Cmd | None = None, parent=None):
        super().__init__(parent)
        self._cmd = cmd

        self.setWindowTitle("双击选择要卸载的应用包名")
        self.resize(400, 500)

        layout = QVBoxLayout(self)
        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)

        button = QPushButton("刷新应用包名列表")
        layout.addWidget(button)

        button.clicked.connect(self.load_package_names)

        self.update_list_signal.connect(self.refresh_list)

        self.list_widget.itemDoubleClicked.connect(self.uninstall_apk)

        self.load_package_names()

    def refresh_list(self, package_list):
        self.list_widget.clear()
        self.list_widget.addItems(package_list)

    def load_package_names(self):
        def handle_output(exit_code, full_output):
            lines = full_output.strip().split("\n")
            packages = [line.replace("package:", "").strip() for line in lines if line.strip()]
            self.update_list_signal.emit(packages)

        self._cmd.run("adb", ["shell", "pm", "list", "packages", "-3"], handle_output)

    def uninstall_apk(self, item):
        package_name = item.text()
        reply = QMessageBox.question(
            self,
            "提示",
            f"确定卸载：\n{package_name} ?"
        )

        if reply == QMessageBox.StandardButton.Yes:
            def uninstall_finished(exit_code, full_output):
                if exit_code == 0:
                    QMessageBox.information(self, "成功", f"{package_name} 卸载成功")
                else:
                    QMessageBox.warning(self, "失败", f"{package_name} 卸载失败")
                self.load_package_names()

            self._cmd.run("adb", ["uninstall", package_name], uninstall_finished)


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

    def _init(self):
        self._ui.adb_devices_pushButton.clicked.connect(self.on_adb_devices_pushButton_clicked)

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

    def on_adb_devices_pushButton_clicked(self):
        self._cmd.run("adb", ["devices"])

    def on_adb_shell_am_force__stop_package_pushButton_clicked(self):
        pass

    def on_install_apk_pushButton_clicked(self):
        file_paths, _ = QFileDialog.getOpenFileNames(
            self,
            "可多选要安装的 apk 文件路径",
            self.APKS_DIR,
            "apk 文件路径 (*.apk)"
        )

        if file_paths:
            total = len(file_paths)
            finished_count = 0
            success_list = []
            fail_dict = {}

            def install_finished(exit_code, full_output, path):
                nonlocal finished_count

                finished_count += 1

                if exit_code == 0:
                    success_list.append(path)
                else:
                    reason = full_output.strip()
                    fail_dict[path] = reason if reason else "未知错误"

                if finished_count == total:
                    success_count = len(success_list)
                    fail_count = len(fail_dict)

                    result_msg = (
                        f"共安装 {total} 个应用\n"
                        f"成功 {success_count} 个\n"
                        f"失败 {fail_count} 个\n\n"
                    )

                    if success_list:
                        result_msg += "安装成功 apk 文件路径：\n"
                        result_msg += "\n".join(success_list)
                        result_msg += "\n\n"

                    if fail_dict:
                        result_msg += "安装失败 apk 文件路径 及 失败原因：\n"
                        for path, reason in fail_dict.items():
                            result_msg += f"apk 文件路径：{path}\n失败原因：{reason}\n\n"

                    QMessageBox.information(self, "安装结果", result_msg)

            for file_path in file_paths:
                self._cmd.run(
                    "adb", ["install", file_path],
                    install_finished, finish_func_kwargs=dict(path=file_path)
                )

    def on_uninstall_apk_pushButton_clicked(self):
        dialog = PackageNamesDialog(self._cmd, self)
        dialog.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    aa = AndroidAssistant()
    aa.show()
    sys.exit(app.exec())
