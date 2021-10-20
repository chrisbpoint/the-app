from pyqtgraph import GraphicsLayoutWidget, LabelItem, PlotDataItem


class YPlotter:

    def __init__(self):
        self._widget = GraphicsLayoutWidget()

        self._label = LabelItem(justify="center")
        self._widget.addItem(self._label)
        self._widget.addItem(LabelItem())

        self._widget.nextRow()

        self._trace = PlotDataItem()
        self._trace_plot = self._widget.addPlot()
        self._trace_plot.addItem(self._trace)

        self._initialize_plots()

    def _initialize_plots(self):
        self._initialize_label()
        self._initialize_trace_plot()

    def _initialize_label(self):
        self.set_acquisition_rate(0.0)

    def _initialize_trace_plot(self):
        self._trace_plot.setMenuEnabled(False)
        self._trace_plot.showAxis("top", show=True)
        self._trace_plot.showAxis("right", show=True)

        [self._trace_plot.getAxis(pos).setStyle(showValues=False, tickLength=0) for
         pos in ["top", "right", "left", "bottom"]]

    @property
    def widget(self):
        return self._widget

    def set_acquisition_rate(self, rate):
        self._label.setText(f"acquisition rate: {rate:2.0f} Hz")
