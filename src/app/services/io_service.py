# import doocspie
from . import doocsmy as doocspie


class IOService:

    class IOException(Exception):

        def __init__(self, err):
            super().__init__("I/O error: " + err)

    @classmethod
    def _read(cls, address):
        try:
            return doocspie.read(address)
        except Exception as err:
            raise cls.IOException(str(err))

    def __init__(self, image_data, adc_data):
        self._image_data = image_data
        self._adc_data = adc_data

    @property
    def image_data(self):
        return self._image_data

    @property
    def adc_data(self):
        return self._adc_data

    def update(self):
        if self._image_data.to_update:
            self._image_data.update(self._read(self._image_data.camera_address))
        if self._adc_data.to_update:
            self._adc_data.update(self._read(self._adc_data.adc_address))
