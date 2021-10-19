from .x_tool_ui import XToolUi


class XTool:

    def __init__(self):
        self._x_tool_ui = XToolUi()

    @property
    def ui(self):
        return self._x_tool_ui
