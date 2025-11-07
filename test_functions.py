import math
import numpy as np

from sine_function import create_sine_wave
from step_function import step_function
from sinc_function import sinc

def test_step_function():
    print("--- Testing step_function ---")
    
    assert step_function(1) == 1
    assert step_function(0) == 1
    assert step_function(-1) == 0
    
    threshold = 5
    assert step_function(5, threshold) == 1
    assert step_function(4.99, threshold) == 0
    
    print("step_function tests passed.")
    print("-" * 30)

def test_sinc_function():
    print("--- Testing sinc_function ---")
    
    assert sinc(0) == 1.0
    
    assert abs(sinc(1) - 0.0) < 1e-7
    assert abs(sinc(-2) - 0.0) < 1e-7
    
    expected_value = 2 / math.pi
    assert abs(sinc(0.5) - expected_value) < 1e-7
    
    print("sinc_function tests passed.")
    print("-" * 30)

def test_sine_wave():
    print("--- Testing create_sine_wave ---")
    
    frequency = 10
    duration = 1.0
    sample_rate = 400 
    time, wave = create_sine_wave(frequency, duration, sample_rate)

    expected_length = int(sample_rate * duration)
    assert len(time) == expected_length
    
    expected_last_time = duration - (1/sample_rate)
    assert abs(time[-1] - expected_last_time) < 1e-9

    assert abs(wave[0] - 0.0) < 1e-7
    assert abs(np.max(wave) - 1.0) < 1e-6 
    assert abs(np.min(wave) - (-1.0)) < 1e-6
    
    print("create_sine_wave tests passed.")
    print("-" * 30)

if __name__ == '__main__':
    test_step_function()
    test_sinc_function()
    test_sine_wave()
    
    print("\n✅ All function tests passed successfully!")