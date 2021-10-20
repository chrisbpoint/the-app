from pyqtgraph import GraphicsLayoutWidget, PlotDataItem


class LoggerPlotter:

    def __init__(self):
        self._widget = GraphicsLayoutWidget()

        self._time_series = PlotDataItem()
        self._time_series_plot = self._widget.addPlot()
        self._time_series_plot.addItem(self._time_series)

        self._initialize_plots()

    def _initialize_plots(self):
        self._time_series_plot.setMenuEnabled(False)
        self._time_series_plot.showAxis("top", show=True)
        self._time_series_plot.showAxis("right", show=True)

        [self._time_series_plot.getAxis(pos).setStyle(showValues=False, tickLength=0) for
         pos in ["top", "right", "left", "bottom"]]

    @property
    def widget(self):
        return self._widget
