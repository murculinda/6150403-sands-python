import numpy as np
from sine_function import create_sine_wave as generate_sine_wave


def test_generate_sine_wave():
    t, y = create_sine_wave(1, 2, 1)
    assert len(t) == 1000
    assert y[0] == 0

    t, y = create_sine_wave(5, 3, 1)
    assert np.isclose(max(y), 3, atol=1e-6)

    t, y = creat_sine_wave(1, 2, -1)
    assert len(t) == 0 and len(y) == 0

    t, y = create_sine_wave(5, 0, 1)
    assert np.allclose(y, 0)