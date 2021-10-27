from doocspie.pyqt import ELogPrinter, show_error

from .app_tool_ui import AppToolUi
from .x_tool import XTool
from .y_tool import YTool
from .logger_tool import LoggerTool


class AppTool:

    APPLICATION_NAME = AppToolUi.APPLICATION_NAME
    VERSION = AppToolUi.VERSION

    def __init__(self, concurrency_service, io_service):
        self._x_tool = XTool(io_service.image_data)
        self._y_tool = YTool(io_service.adc_data)
        self._logger_tool = LoggerTool()
        self._app_tool_ui = AppToolUi(self._x_tool.ui, self._y_tool.ui, self._logger_tool.ui)
        self._e_log_printer = ELogPrinter(self._app_tool_ui, printer="fl1_camplog", print_exceptions=True)
        self._concurrency_service = concurrency_service(self._io_and_plot_loop)
        self._io_service = io_service
        self._create_connections()

    def _create_connections(self):
        self._create_app_tool_ui_connections()
        self._create_x_tool_connections()
        self._create_y_tool_connections()

    def _create_app_tool_ui_connections(self):
        self._app_tool_ui.print_to_e_log_action.triggered.connect(self._e_log_printer.show_dialog)

    def _create_x_tool_connections(self):
        self._x_tool.ui.start_button.clicked.connect(self._start_io_and_plot_loop)
        self._x_tool.ui.stop_button.clicked.connect(self._stop_io_and_plot_loop)

    def _create_y_tool_connections(self):
        self._y_tool.ui.start_button.clicked.connect(self._start_io_and_plot_loop)
        self._y_tool.ui.stop_button.clicked.connect(self._stop_io_and_plot_loop)

    def _start_io_and_plot_loop(self):
        if not self._concurrency_service.is_active():
            self._concurrency_service.start()

    def _io_and_plot_loop(self):
        self._update_services()
        self._update_tools()

    def _update_services(self):
        try:
            self._io_service.update()
        except self._io_service.IOException as err:
            self._stop_all_tools()
            show_error(str(err))

    def _stop_all_tools(self):
        self._x_tool.ui.stop_button.click()
        self._y_tool.ui.stop_button.click()

    def _update_tools(self):
        active_ui = self._app_tool_ui.tab_widget.currentWidget()
        if active_ui == self._x_tool.ui:
            self._x_tool.update()
        if active_ui == self._y_tool.ui:
            self._y_tool.update()

    def _stop_io_and_plot_loop(self):
        if self._concurrency_service.is_active() and self._all_tools_have_stopped():
            self._concurrency_service.stop()

    def _all_tools_have_stopped(self):
        return not (self._x_tool.is_started or self._y_tool.is_started)

    def show_window(self):
        self._app_tool_ui.show_window()
