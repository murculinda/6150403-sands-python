import numpy as np
from sine_function import create_sine_wave

def test_create_sine_wave():
    t, y = create_sine_wave(1, 1, 1000) 
    assert len(t) == 1000
    assert y[0] == 0

    t, y = create_sine_wave(5, 3, 1000) # Using a high sample rate for accurate max value
    assert np.isclose(max(y), 1.0, atol=1e-6)

    t, y = create_sine_wave(1, -1, 1000)
    assert len(t) == 0 and len(y) == 0

    t, y = create_sine_wave(0, 1, 1000) 
    assert np.allclose(y, 0)

def test_we_want_to_see_a_fail():
    
    t, y = create_sine_wave(1, 2, 1)
    
    assert len(t) == 999