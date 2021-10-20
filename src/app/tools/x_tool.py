from .x_tool_ui import XToolUi


class XTool:

    def __init__(self):
        self._x_tool_ui = XToolUi()
        self._create_connections()

    def _create_connections(self):
        self._x_tool_ui.start_button.clicked.connect(self._start_button_clicked)
        self._x_tool_ui.stop_button.clicked.connect(self._stop_button_clicked)

    def _start_button_clicked(self):
        ...

    def _stop_button_clicked(self):
        ...

    @property
    def ui(self):
        return self._x_tool_ui
