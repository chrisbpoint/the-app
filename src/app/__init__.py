import os
import signal
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

from src.app.tools.app_tool import AppTool


def startup_application():
    signal.signal(signal.SIGINT, signal.SIG_DFL)  # handles Ctrl-C interrupts via default signal (core dump and exit)

    application = QApplication([AppTool.APPLICATION_NAME])
    application.setWindowIcon(QIcon(os.path.dirname(os.path.abspath(__file__)) + "/resources/app.png"))

    app_tool = AppTool()
    app_tool.show_window()

    sys.exit(application.exec())
