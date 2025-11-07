# Step and Sinc Functions (Python)

This repository contains two simple mathematical function implementations:

- **Step Function** (`step_function.py`)
- **Sinc Function** (`sinc_function.py`)

These functions are commonly used in signal processing, control systems, and mathematical modeling.

---

## 📁 Files

| File | Description |
|------|-------------|
| `step_function.py` | Implements a step function that returns 1 if `x >= threshold`, otherwise 0. |
| `sinc_function.py` | Implements the sinc function: `sin(πx) / (πx)` with proper handling at `x = 0`. |

---

## 🧠 Usage

### Step Function
```python
from step_function import step_function

print(step_function(2))     # Output: 1
print(step_function(-1))    # Output: 0
```

### Sinc Function
```python
from sinc_function import sinc

print(sinc(0))     # Output: 1.0
print(sinc(1))     # Output: ~0.318
```

---

## 🔧 Requirements

- Python 3.x

No external dependencies are required.

---

## 📜 License

This project is released under the MIT License. Feel free to use and modify.
