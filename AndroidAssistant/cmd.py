from PySide6.QtCore import QObject, QProcess, Signal

from logger import Logger


class Cmd(QObject):
    outputReceived = Signal(str)
    finished = Signal(int, str)  # code, output

    def __init__(self, logger: Logger | None = None, use_logger: bool = True):
        super().__init__()
        self._logger: Logger | None = logger
        self._use_logger = use_logger

        self._times: int = 0
        self._processes: list[QProcess] = []

    def run(self, program: str, program_args: list, callback=None, callback_kwargs=None, use_logger=True):
        process = QProcess(self)
        output = ""
        cmd_str = f"{program} {' '.join(program_args)}"

        process.setProcessChannelMode(QProcess.ProcessChannelMode.SeparateChannels)

        def on_stdout():
            nonlocal output
            data = process.readAllStandardOutput().data().decode()
            output += data
            self.outputReceived.emit(data)
            if use_logger and self._logger:
                self._logger.debug(data, tag=tag)

        def on_stderr():
            nonlocal output
            data = process.readAllStandardError().data().decode()
            output += data
            self.outputReceived.emit(data)
            if use_logger and self._logger:
                self._logger.debug(data, tag=tag)

        def on_finished(code):
            if callback:
                if callback_kwargs:
                    callback(code, output, **callback_kwargs)
                else:
                    callback(code, output)
            self.finished.emit(code, output)
            self._processes.remove(process)
            if use_logger and self._logger:
                if code == 0:
                    self._logger.success(f"{cmd_str} exited with code {code}", tag=tag)
                else:
                    self._logger.error(f"{cmd_str} exited with code {code}", tag=tag)

        process.readyReadStandardOutput.connect(on_stdout)
        process.readyReadStandardError.connect(on_stderr)
        process.finished.connect(on_finished)

        if use_logger and self._logger:
            self._times += 1
            tag = f"[{self._times}]"
            self._logger.info(cmd_str, tag=tag)

        process.start(program, program_args)
        self._processes.append(process)
