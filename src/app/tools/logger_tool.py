from collections import namedtuple

import numpy as np

from .logger_tool_ui import LoggerToolUi


class LoggerTool:

    _TimeSeries = namedtuple("TimeSeries", ["shots", "values"])

    def __init__(self, metrics_data):
        self._logger_tool_ui = LoggerToolUi()
        self._metrics_data = metrics_data

    @property
    def ui(self):
        return self._logger_tool_ui

    def initialize(self):
        self._metrics_data.initialize()

    def update(self):
        if self._metrics_data.is_new_data_available:
            time_series = self._TimeSeries(np.arange(1, len(self._metrics_data.peaks) + 1), self._metrics_data.peaks)
            self._logger_tool_ui.plot_time_series(time_series)
