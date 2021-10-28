class MetricsService:

    def __init__(self, adc_data, metrics_data):
        self._adc_data = adc_data
        self._metrics_data = metrics_data

    @property
    def metrics_data(self):
        return self._metrics_data

    def update(self):
        self._metrics_data.is_new_data_available = False
        if self._adc_data.is_new_data_available:
            self._metrics_data.update(self._adc_data.trace)
            self._metrics_data.is_new_data_available = True
