from .y_tool_ui import YToolUi


class YTool:

    def __init__(self):
        self._y_tool_ui = YToolUi()

    @property
    def ui(self):
        return self._y_tool_ui
