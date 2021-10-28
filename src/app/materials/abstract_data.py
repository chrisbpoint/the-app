import time
from abc import ABC, abstractmethod


class AbstractData(ABC):

    def __init__(self, address):
        self._address = address
        self._acquisition_rate = None
        self._to_update = None
        self._is_new_data_available = None
        self._event = None
        self._to_initialize = None
        self._data_dict = None
        self._last_update = None

    @property
    def address(self):
        return self._address

    @property
    def acquisition_rate(self):
        return self._acquisition_rate

    @property
    def to_update(self):
        return self._to_update

    @property
    def is_new_data_available(self):
        return self._is_new_data_available

    def initialize(self):
        self._to_update = True
        self._to_initialize = True

    def reset(self):
        self._to_update = False
        self._is_new_data_available = False

    def update(self, data_readout):
        if self._to_initialize:
            self._initialize(data_readout.event)
        self._data_dict = data_readout
        data_dict_event = self._data_dict.event
        self._is_new_data_available = False
        if data_dict_event != self._event:
            self._update_acquisition_rate()
            self._update_data()
            self._event = data_dict_event
            self._is_new_data_available = True

    def _initialize(self, event):
        self._event = event
        self._last_update = time.time()
        self._to_initialize = False

    def _update_acquisition_rate(self):
        current_update = time.time()
        self._acquisition_rate = 1 / (current_update - self._last_update)
        self._last_update = current_update

    @abstractmethod
    def _update_data(self):
        pass
