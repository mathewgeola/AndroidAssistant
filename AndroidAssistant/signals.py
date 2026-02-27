from PySide6.QtCore import QObject, Signal


class Signals(QObject):
    adb_shell_pm_list_packages = Signal()
