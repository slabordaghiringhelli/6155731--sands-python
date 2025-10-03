import numpy as np
import matplotlib.pyplot as plt
from  signals_and_systems import create_sine_wave


sine_wave_1 = create_sine_wave(2,2)
sine_wave_2 = create_sine_wave(5,2)
sine_wave_3 = create_sine_wave(8,2)
sine_wave_4 = create_sine_wave(1,4)


plt.figure()
plt.xlim((0,30000))
plt.plot(sine_wave_1, label="sine wave 1")
plt.plot(sine_wave_2, label="sine wave 2")
plt.plot(sine_wave_3, 'g:', label="sine wave 3")
plt.plot(sine_wave_4, 'r:', label="sine wave 4")
plt.xlabel("Time(seconds)")
plt.ylabel("Amplitude")
plt.title("sine waves plotted")
plt.legend()
plt.show()



print("hello") 

print("Sergi is testing")
