print("Hello!")


import numpy as np
import matplotlib.pyplot as plt



def create_sine_wave(frequency, duration):
    t = np.linspace(0, duration, int(44100 * duration))
    return np.sin(2 * np.pi * frequency * t)
    


sine_wave = create_sine_wave(440, 2)



plt.plot(sine_wave)
plt.xlabel("Time(seconds)")
plt.ylabel("Amplitude")
plt.title("Sine wave")
plt.show()

print("hello")



