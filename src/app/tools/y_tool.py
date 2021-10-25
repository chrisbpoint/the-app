from .y_tool_ui import YToolUi


class YTool:

    def __init__(self, adc_data):
        self._y_tool_ui = YToolUi()
        self._adc_data = adc_data
        self._is_started = False
        self._create_connections()

    def _create_connections(self):
        self._y_tool_ui.start_button.clicked.connect(self._start_button_clicked)
        self._y_tool_ui.stop_button.clicked.connect(self._stop_button_clicked)

    @property
    def ui(self):
        return self._y_tool_ui

    @property
    def is_started(self):
        return self._is_started

    def _start_button_clicked(self):
        self._y_tool_ui.start_button.setEnabled(False)
        self._y_tool_ui.start_button.setText("running ...")
        self._adc_data.initialize()
        self._is_started = True

    def _stop_button_clicked(self):
        if self._is_started:
            self._is_started = False
            self._adc_data.reset()
            self._y_tool_ui.start_button.setText(YToolUi.START)
            self._y_tool_ui.start_button.setEnabled(True)
            self._y_tool_ui.update_acquisition_rate(0.0)

    def update(self):
        print(4)