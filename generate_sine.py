import numpy as np
import soundfile as sf

if __name__ == "__main__":
    sample_rate = 44100  # in Hz
    duration = 5.0  # in seconds
    frequency = 440.0  # in Hz (A4 note)

    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    sine_wave = 0.5 * np.sin(2 * np.pi * frequency * t)  # 0.5 to avoid clipping

    sf.write("sine_440hz.wav", sine_wave, sample_rate)
    print("Sine wave saved as sine_440hz.wav")
