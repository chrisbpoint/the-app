from doocspie.pyqt import ELogPrinter

from .app_tool_ui import AppToolUi
from .x_tool import XTool
from .y_tool import YTool
from .logger_tool import LoggerTool


class AppTool:

    APPLICATION_NAME = AppToolUi.APPLICATION_NAME
    VERSION = AppToolUi.VERSION

    def __init__(self):
        self._x_tool = XTool()
        self._y_tool = YTool()
        self._logger_tool = LoggerTool()
        self._app_tool_ui = AppToolUi(self._x_tool.ui, self._y_tool.ui, self._logger_tool.ui)
        self._e_log_printer = ELogPrinter(self._app_tool_ui, printer="fl1_camplog", print_exceptions=True)
        self._create_connections()

    def _create_connections(self):
        self._create_app_tool_ui_connections()

    def _create_app_tool_ui_connections(self):
        self._app_tool_ui.print_to_e_log_action.triggered.connect(self._e_log_printer.show_dialog)

    def show_window(self):
        self._app_tool_ui.show_window()
