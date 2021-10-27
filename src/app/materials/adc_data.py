from .abstract_data import AbstractData


class AdcData(AbstractData):

    def __init__(self, address):
        super().__init__(address)
        self._trace = None

    @property
    def trace(self):
        return self._trace

    def _update_data(self):
        self._trace = self._data_dict.data
