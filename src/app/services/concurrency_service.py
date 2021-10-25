from PyQt5.QtCore import QTimer


class ConcurrencyService:

    def __init__(self):
        self._timer = QTimer()
        self._function = None

    def __call__(self, function):
        self._function = function
        return self

    def start(self):
        self._timer.timeout.connect(self._function)
        self._timer.start(0)

    def stop(self):
        self._timer.stop()
        self._timer.timeout.disconnect(self._function)

    def is_active(self):
        return self._timer.isActive()
