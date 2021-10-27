import os
import signal
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon

from .tools.app_tool import AppTool
from .services.concurrency_service import ConcurrencyService
from .services.io_service import IOService
from .materials.image_data import ImageData
from .materials.adc_data import AdcData


def startup_application():
    signal.signal(signal.SIGINT, signal.SIG_DFL)  # handles Ctrl-C interrupts via default signal (core dump and exit)

    application = QApplication([AppTool.APPLICATION_NAME])
    application.setWindowIcon(QIcon(os.path.dirname(os.path.abspath(__file__)) + "/resources/app.png"))

    image_data = ImageData(address="image_address")
    adc_data = AdcData(address="adc_address")

    concurrency_service = ConcurrencyService()
    io_service = IOService(image_data, adc_data)

    app_tool = AppTool(concurrency_service, io_service)
    app_tool.show_window()

    sys.exit(application.exec())
