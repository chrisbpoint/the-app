from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QAction, QTabWidget

from doocspie.pyqt import show_about


class AppToolUi(QMainWindow):

    APPLICATION_NAME = "App"
    VERSION = "0.0.1"

    def __init__(self, *tool_uis):
        super().__init__()
        self._tool_uis = tool_uis
        self._main_layout = QVBoxLayout()
        self._print_to_e_log_action = QAction("Print to E-Log")
        self._click_about_action = QAction("About")
        self._tab_widget = QTabWidget()
        self._create_layout()
        self._create_connections()

    def _create_layout(self):
        self._create_main_layout()
        self._create_menu_bar()
        self._create_tools_tab_widget()

    def _create_main_layout(self):
        main_widget = QWidget()
        main_widget.setLayout(self._main_layout)
        self.setCentralWidget(main_widget)

    def _create_menu_bar(self):
        self._create_file_menu()
        self._create_help_menu()

    def _create_file_menu(self):
        self.menuBar().addMenu("File").addAction(self._print_to_e_log_action)

    def _create_help_menu(self):
        self.menuBar().addMenu("Help").addAction(self._click_about_action)

    def _create_tools_tab_widget(self):
        for tool_ui in self._tool_uis:
            self._tab_widget.addTab(tool_ui, tool_ui.NAME)
        self._main_layout.addWidget(self._tab_widget)

    def _create_connections(self):
        self._click_about_action.triggered.connect(lambda: show_about(self, self.APPLICATION_NAME, self.VERSION))

    @property
    def print_to_e_log_action(self):
        return self._print_to_e_log_action

    def show_window(self):
        self.show()
        self.setMinimumSize(self.width(), self.height())
