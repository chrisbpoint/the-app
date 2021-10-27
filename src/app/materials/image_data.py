from collections import namedtuple

import numpy as np

from .abstract_data import AbstractData


class ImageData(AbstractData):

    _Data = namedtuple("Data", ["x", "y"])

    def __init__(self, address):
        super().__init__(address)
        self._image = None
        self._projection = None

    @property
    def image(self):
        return self._image

    @property
    def projection(self):
        return self._projection

    def _update_data(self):
        self._image = self._data_dict.data
        self._projection = self._Data(np.arange(0, len(np.nansum(self._image, axis=1))),
                                      np.nansum(self._image, axis=1))
