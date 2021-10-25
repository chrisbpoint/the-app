class ImageData:

    def __init__(self, camera_address):
        self._camera_address = camera_address
        self._to_update = None

    @property
    def camera_address(self):
        return self._camera_address

    @property
    def to_update(self):
        return self._to_update

    def initialize(self):
        self._to_update = True

    def reset(self):
        self._to_update = False

    def update(self, image_readout):
        print(1)