from PySide6.QtCore import QObject, QProcess, Signal

from logger import Logger


class Cmd(QObject):
    outputReceived = Signal(str)
    finished = Signal(int, str)  # exit_code, full_output

    def __init__(self, logger: Logger | None = None, use_logger: bool = True):
        super().__init__()
        self._logger: Logger | None = logger
        self._use_logger = use_logger

        self._process: QProcess | None = None
        self._cmd: str | None = None
        self._buffer: str | None = None

        self._times: int = 0
        self._processes: list[QProcess] = []

    def run(self, program: str, args: list, finish_func=None, finish_func_kwargs=None, use_logger=True):
        process = QProcess(self)
        buffer = ""
        cmd_str = f"{program} {' '.join(args)}"

        process.setProcessChannelMode(QProcess.ProcessChannelMode.SeparateChannels)

        def on_stdout():
            nonlocal buffer
            data = process.readAllStandardOutput().data().decode()
            buffer += data
            self.outputReceived.emit(data)
            if use_logger and self._logger:
                self._logger.debug(data, tag=tag)

        def on_stderr():
            nonlocal buffer
            data = process.readAllStandardError().data().decode()
            buffer += data
            self.outputReceived.emit(data)
            if use_logger and self._logger:
                self._logger.debug(data, tag=tag)

        def on_finished(exit_code):
            if finish_func:
                if finish_func_kwargs:
                    finish_func(exit_code, buffer, **finish_func_kwargs)
                else:
                    finish_func(exit_code, buffer)
            self.finished.emit(exit_code, buffer)
            self._processes.remove(process)
            if use_logger and self._logger:
                if exit_code == 0:
                    self._logger.success(f"{cmd_str} exited with code {exit_code}", tag=tag)
                else:
                    self._logger.error(f"{cmd_str} exited with code {exit_code}", tag=tag)

        process.readyReadStandardOutput.connect(on_stdout)
        process.readyReadStandardError.connect(on_stderr)
        process.finished.connect(on_finished)

        if use_logger and self._logger:
            self._times += 1
            tag = f"[{self._times}]"
            self._logger.info(cmd_str, tag=tag)

        process.start(program, args)
        self._processes.append(process)
