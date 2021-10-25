from .x_tool_ui import XToolUi


class XTool:

    def __init__(self, image_data):
        self._x_tool_ui = XToolUi()
        self._image_data = image_data
        self._is_started = False
        self._create_connections()

    def _create_connections(self):
        self._x_tool_ui.start_button.clicked.connect(self._start_button_clicked)
        self._x_tool_ui.stop_button.clicked.connect(self._stop_button_clicked)

    @property
    def ui(self):
        return self._x_tool_ui

    @property
    def is_started(self):
        return self._is_started

    def _start_button_clicked(self):
        self._x_tool_ui.start_button.setEnabled(False)
        self._x_tool_ui.start_button.setText("running ...")
        self._image_data.initialize()
        self._is_started = True

    def _stop_button_clicked(self):
        if self._is_started:
            self._is_started = False
            self._image_data.reset()
            self._x_tool_ui.start_button.setText(XToolUi.START)
            self._x_tool_ui.start_button.setEnabled(True)
            self._x_tool_ui.update_acquisition_rate(0.0)

    def update(self):
        print(3)
