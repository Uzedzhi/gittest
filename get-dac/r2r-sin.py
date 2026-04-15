import numpy
import time
import math

def get_sin_wave_amplitude(freq, t):
    return (math.sin(2 * math.pi * freq * t) + 1) / 2