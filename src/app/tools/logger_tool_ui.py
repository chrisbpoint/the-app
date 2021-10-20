from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout

from ..plotter.logger_plotter import LoggerPlotter


class LoggerToolUi(QMainWindow):

    NAME = "Logger"

    def __init__(self):
        super().__init__()
        self._main_layout = QVBoxLayout()
        self._logger_plotter = LoggerPlotter()
        self._create_layout()

    def _create_layout(self):
        self._create_main_layout()
        self._create_plot_layout()

    def _create_main_layout(self):
        main_widget = QWidget()
        main_widget.setLayout(self._main_layout)
        self.setCentralWidget(main_widget)

    def _create_plot_layout(self):
        plot_layout = QHBoxLayout()
        plot_layout.addWidget(self._logger_plotter.widget)
        self._main_layout.addLayout(plot_layout)
