class AdcData:

    def __init__(self, adc_address):
        self._adc_address = adc_address
        self._to_update = None

    @property
    def adc_address(self):
        return self._adc_address

    @property
    def to_update(self):
        return self._to_update

    def initialize(self):
        self._to_update = True

    def reset(self):
        self._to_update = False

    def update(self, adc_readout):
        print(2)