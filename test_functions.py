from sine_function import sine
from step_function import step_function
from sinc_function import sinc

# ---- Tests for sine function ----
assert round(sine(0), 5) == 0
assert round(sine(3.14159265/2), 5) == 1.0

# ---- Tests for step function ----
assert step_function(-1) == 0
assert step_function(0) == 1
assert step_function(5, threshold=2) == 1
assert step_function(1, threshold=2) == 0

# ---- Tests for sinc function ----
assert sinc(0) == 1.0
assert round(sinc(1), 5) == round(0.318309886, 5)
assert round(sinc(-1), 5) == round(-0.318309886, 5)

print("✅ All tests passed!")
