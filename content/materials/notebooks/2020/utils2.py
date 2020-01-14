import numpy as np

def period2freq(period):
    """Returns frequency in rad/s given period in seconds."""
    return 1.0 / period * 2.0 * np.pi

def freq2period(freq):
    """Returns period in seconds given frequency in rads/."""
    return 1.0 / freq * 2.0 * np.pi