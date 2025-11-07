from sinc_function import sinc
import math 

def test_sinc_function():

    assert np.isclose(sinc(1), 0)

    assert np.isclose(sinc(1), 0)
    assert np.isclose(sinc(-2), 0)
    
    expected_val = 2 / math.pi
    actual_val = sinc(0.5)
    assert np.isclose(actual_val, expected_val, atol=1e-9)