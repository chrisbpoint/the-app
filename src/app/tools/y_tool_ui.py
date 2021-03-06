from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QPushButton, QWidget, QHBoxLayout, QGroupBox

from ..plotter.y_plotter import YPlotter


class YToolUi(QMainWindow):

    NAME = "Y"

    START = "Start"

    def __init__(self):
        super().__init__()
        self._main_layout = QVBoxLayout()
        self._y_plotter = YPlotter()
        self._start_button = QPushButton(self.START)
        self._stop_button = QPushButton("Stop")
        self._create_layout()

    def _create_layout(self):
        self._create_main_layout()
        self._create_plot_layout()
        self._create_controls_layout()

    def _create_main_layout(self):
        main_widget = QWidget()
        main_widget.setLayout(self._main_layout)
        self.setCentralWidget(main_widget)

    def _create_plot_layout(self):
        plot_layout = QHBoxLayout()
        plot_layout.addWidget(self._y_plotter.widget)
        self._main_layout.addLayout(plot_layout)

    def _create_controls_layout(self):
        controls_layout = QHBoxLayout()
        controls_layout.addWidget(self._create_control_group_box())
        self._main_layout.addLayout(controls_layout)

    def _create_control_group_box(self):
        group_box = QGroupBox("Control")
        widgets_layout = QHBoxLayout()
        widgets_layout.addWidget(self._start_button)
        widgets_layout.addWidget(self._stop_button)
        group_box.setLayout(widgets_layout)
        return group_box

    @property
    def start_button(self):
        return self._start_button

    @property
    def stop_button(self):
        return self._stop_button

    def plot_trace(self, trace):
        self._y_plotter.set_trace(trace)

    def update_acquisition_rate(self, rate):
        self._y_plotter.set_acquisition_rate(rate)
