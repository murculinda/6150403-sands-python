import numpy as np
import matplotlib.pyplot as plt

def sinus_function(frequency, duration):
	t = np.linspace(0, duration, int(44100 * duration))
	y = np.sin(2 * np.pi * frequency * t)
	return t, y

t, y = create_sine_wave(10, 5)

plt.plot(t, y)

plt.xlabel("Time(s)")

plt.ylabel("Amplitude")

plt.title("Sine Wave")

plt.show()