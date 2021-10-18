from PyQt5.QtWidgets import QMainWindow


class AppToolUi(QMainWindow):

    APPLICATION_NAME = "App"
    VERSION = "0.0.1"

    def __init__(self):
        super().__init__()

    def show_window(self):
        self.show()
