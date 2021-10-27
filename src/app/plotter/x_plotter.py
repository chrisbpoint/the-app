from pyqtgraph import setConfigOptions, GraphicsLayoutWidget, LabelItem, ImageItem, PlotDataItem


class XPlotter:

    setConfigOptions(imageAxisOrder="row-major")

    def __init__(self):
        self._widget = GraphicsLayoutWidget()

        self._label = LabelItem(justify="center")
        self._widget.addItem(self._label)
        self._widget.addItem(LabelItem())

        self._widget.nextRow()
        self._image = ImageItem()
        self._image_plot = self._widget.addPlot()
        self._image_plot.addItem(self._image)

        self._projection = PlotDataItem()
        self._projection_plot = self._widget.addPlot()
        self._projection_plot.addItem(self._projection)

        self._initialize_plots()

    def _initialize_plots(self):
        self._initialize_label()
        self._initialize_image_plot()
        self._initialize_projection_plot()

    def _initialize_label(self):
        self.set_acquisition_rate(0.0)

    def _initialize_image_plot(self):
        self._image_plot.setMenuEnabled(False)
        self._image_plot.setMinimumWidth(400)
        self._image_plot.showAxis("top", show=True)
        self._image_plot.showAxis("right", show=True)

        [self._image_plot.getAxis(pos).setStyle(showValues=False, tickLength=0) for
         pos in ["top", "right", "left", "bottom"]]

        self._image_plot.invertY(True)

    def _initialize_projection_plot(self):
        self._projection_plot.setMenuEnabled(False)
        self._projection_plot.setMouseEnabled(False, False)
        self._projection_plot.hideButtons()
        self._projection_plot.setMaximumWidth(200)
        self._projection_plot.showAxis("top", show=True)
        self._projection_plot.showAxis("right", show=True)

        [self._projection_plot.getAxis(pos).setStyle(showValues=False, tickLength=0) for
         pos in ["top", "right", "left", "bottom"]]

        self._projection_plot.invertY(True)

    @property
    def widget(self):
        return self._widget

    def set_image(self, image):
        self._image.setImage(image)

    def set_projection(self, projection):
        self._projection.setData(projection.y, projection.x)
        self._projection_plot.setYRange(*self._image_plot.getAxis("left").range, padding=0)

    def set_acquisition_rate(self, rate):
        self._label.setText(f"acquisition rate: {rate:2.0f} Hz")
