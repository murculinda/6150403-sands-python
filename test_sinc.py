from sinc_function import sinc
import math 

def test_sinc_function():

    assert sinc(0) == 1.0

    assert sinc(1) == 0
    assert sinc(-2) == 0
    
    expected_val = 2 / math.pi
    actual_val = sinc(0.5)
    # Use np.isclose for floating-point comparison
    assert np.isclose(actual_val, expected_val, atol=1e-9)