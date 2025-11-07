import numpy as np

def create_sine_wave(frequency, duration_seconds, sample_rate=1000):
    """
    Generates a sine wave array using NumPy.

    Parameters:
        frequency (float): The frequency of the wave in Hertz (Hz).
        duration_seconds (float): The total length of the wave in seconds.
        sample_rate (int): The number of samples per second (default 1000).

    Returns:
        tuple: (time_array, amplitude_array)
    """

    t = np.linspace(0, duration_seconds, int(sample_rate * duration_seconds), endpoint=False)
    
  
    amplitude = np.sin(2 * np.pi * frequency * t)
    
    return t, amplitude

if __name__ == "__main__":
   
    try:
        import matplotlib.pyplot as plt
        

        time, wave = create_sine_wave(frequency=440, duration_seconds=1.0)
        
        plt.figure(figsize=(10, 4))
        plt.plot(time, wave)
        plt.title('440 Hz Sine Wave')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.show()

    except ImportError:
        print("Matplotlib not installed. Cannot show plot.")
    
    t, wave = create_sine_wave(frequency=1, duration_seconds=1, sample_rate=4)
    print(f"Time array: {t}")
    print(f"Wave array: {wave}")