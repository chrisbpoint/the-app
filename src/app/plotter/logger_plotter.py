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

    def set_time_series(self, time_series):
        self._time_series_plot.getAxis("bottom").setStyle(showValues=True)
        self._time_series_plot.setLabel("bottom", "Shot number")
        self._time_series_plot.getAxis("left").setStyle(showValues=True)
        self._time_series_plot.setLabel("left", "Values (px)")

        self._time_series.setData(time_series.shots, time_series.values)
