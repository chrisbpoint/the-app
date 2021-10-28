import numpy as np


class MetricsData:

    def __init__(self):
        self._is_new_data_available = None
        self._initialized = None
        self._peaks = list()

    @property
    def is_new_data_available(self):
        return self._is_new_data_available

    @is_new_data_available.setter
    def is_new_data_available(self, state):
        self._is_new_data_available = state

    @property
    def peaks(self):
        return self._peaks

    def initialize(self):
        self._peaks.clear()

    def update(self, adc_data_trace):
        self._peaks.append(np.argmax(adc_data_trace))
