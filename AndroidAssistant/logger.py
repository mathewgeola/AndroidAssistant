import datetime
import html
import os
import subprocess
import sys

from PySide6.QtCore import QObject, Signal, QUrl
from PySide6.QtGui import QTextCursor
from PySide6.QtWidgets import QApplication, QTextBrowser


class Logger(QObject):
    log_signal = Signal(str, str, bool)

    def __init__(self, text_browser: QTextBrowser, log_file_path: str | None = None):
        super().__init__()
        self.text_browser = text_browser
        self.log_file_path = log_file_path

        app = QApplication.instance()
        if app:
            app.aboutToQuit.connect(self.close)

        self.log_signal.connect(self._handle_log_signal)

        self.text_browser.setOpenExternalLinks(False)
        self.text_browser.setOpenLinks(False)
        self.text_browser.anchorClicked.connect(self._handle_anchorClicked)

        if self.log_file_path:
            self._file = open(self.log_file_path, "a", encoding="utf-8")
        else:
            self._file = None

    def _handle_log_signal(self, text: str, color: str, is_html: bool) -> None:
        if not is_html:
            safe_text = html.escape(text)
        else:
            safe_text = text
        html_text = f'<span style="color:{color};">{safe_text}</span>'

        self.text_browser.append(html_text)
        self.text_browser.moveCursor(QTextCursor.End)  # noqa

    @staticmethod
    def _handle_anchorClicked(url: QUrl) -> None:  # noqa
        if not url or not url.isValid():
            return

        path = url.toLocalFile()
        if not path:
            return

        path = os.path.normpath(path)

        if not os.path.exists(path):
            return

        if sys.platform.startswith("win"):
            if os.path.isfile(path):
                subprocess.Popen(
                    ["explorer", "/select,", path],
                    shell=False
                )
            else:
                subprocess.Popen(
                    ["explorer", path],
                    shell=False
                )

        elif sys.platform == "darwin":
            if os.path.isfile(path):
                subprocess.Popen(["open", "-R", path])
            else:
                subprocess.Popen(["open", path])

        else:
            if os.path.isfile(path):
                folder = os.path.dirname(path)
                subprocess.Popen(["xdg-open", folder])
            else:
                subprocess.Popen(["xdg-open", path])

    def _log(self, level: str, msg: str, color: str, is_html: bool = False, tag: str = "[*]") -> None:
        datetime_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        full_msg = f"{datetime_str} {level} {tag} {msg}"

        self.log_signal.emit(full_msg, color, is_html)

        if self._file:
            self._file.write(full_msg + "\n")
            self._file.flush()

    def debug(self, msg: str, is_html: bool = False, tag: str = "[*]") -> None:
        self._log("DEBUG    ", msg, "gray", is_html, tag)

    def info(self, msg: str, is_html: bool = False, tag: str = "[*]") -> None:
        self._log("INFO     ", msg, "black", is_html, tag)

    def success(self, msg: str, is_html: bool = False, tag: str = "[*]") -> None:
        self._log("SUCCESS  ", msg, "green", is_html, tag)

    def warning(self, msg: str, is_html: bool = False, tag: str = "[*]") -> None:
        self._log("WARNING  ", msg, "orange", is_html, tag)

    def error(self, msg: str, is_html: bool = False, tag: str = "[*]") -> None:
        self._log("ERROR    ", msg, "red", is_html, tag)

    def close(self) -> None:
        if self._file and not self._file.closed:
            self._file.flush()
            self._file.close()
