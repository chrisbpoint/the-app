from .logger_tool_ui import LoggerToolUi


class LoggerTool:

    def __init__(self):
        self._logger_tool_ui = LoggerToolUi()

    @property
    def ui(self):
        return self._logger_tool_ui
