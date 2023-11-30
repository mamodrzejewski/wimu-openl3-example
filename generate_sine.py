import numpy as np
from scipy.io import wavfile

sr = 44100
freq = 440
duration = 5

t = np.linspace(0, duration, sr * duration)
y = np.sin(freq * 2 * np.pi * t)

wavfile.write('440_sine.wav', sr, y)