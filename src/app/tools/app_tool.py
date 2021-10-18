from .app_tool_ui import AppToolUi


class AppTool:

    APPLICATION_NAME = AppToolUi.APPLICATION_NAME
    VERSION = AppToolUi.VERSION

    def __init__(self):
        self._app_tool_ui = AppToolUi()

    def show_window(self):
        self._app_tool_ui.show_window()
