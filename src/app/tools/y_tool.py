from .y_tool_ui import YToolUi


class YTool:

    def __init__(self):
        self._y_tool_ui = YToolUi()
        self._create_connections()

    def _create_connections(self):
        self._y_tool_ui.start_button.clicked.connect(self._start_button_clicked)
        self._y_tool_ui.stop_button.clicked.connect(self._stop_button_clicked)

    def _start_button_clicked(self):
        ...

    def _stop_button_clicked(self):
        ...

    @property
    def ui(self):
        return self._y_tool_ui
