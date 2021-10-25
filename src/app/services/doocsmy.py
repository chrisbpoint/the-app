import time

import numpy as np


img_event = 0
trace_event = 0
img_start = time.time()
trace_start = time.time()
img_peak = np.zeros([800, 800])

for i in range(img_peak.shape[0]):
    for j in range(img_peak.shape[1]):
        img_peak[i, j] += 1*np.exp(-(i-200)**2/2/10**2 - (j-300)**2/2/50**2)


def read(address):
    global img_event, trace_event, img_start, trace_start, img_old, trace_old, img_peak

    if address == "image_address":
        img = (100 + 0.1 * np.random.randn(*img_peak.shape)) + img_peak

        if img_event != 0 and time.time() - img_start < 0.2:
            return Readout({'data': img_old, "timestamp": time.time(), "macropulse": img_event})
        else:
            img_start = time.time()
            img_old = img.copy()
            img_event += 1
            return Readout({'data': img_old, "timestamp": time.time(), "macropulse": img_event})

    elif address == "adc_address":
        trace = (100 + 0.1 * np.random.randn(1000))

        trace += np.exp(-(np.arange(len(trace))-500+np.random.randn()*50)**2/2/10**2)

        if trace_event != 0 and time.time() - trace_start < 0.1:
            return Readout({'data': trace_old, "timestamp": time.time(), "macropulse": trace_event})
        else:
            trace_start = time.time()
            trace_old = trace.copy()
            trace_event += 1
            return Readout({'data': trace_old, "timestamp": time.time(), "macropulse": trace_event})


class Readout:

    def __init__(self, pydoocs_output):
        self._data = pydoocs_output["data"]
        self._timestamp = pydoocs_output["timestamp"]
        self._event = pydoocs_output["macropulse"]

    @property
    def data(self):
        return self._data

    @property
    def timestamp(self):
        return self._timestamp

    @property
    def event(self):
        return self._event
