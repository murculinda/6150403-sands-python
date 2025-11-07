import math

def sinc(x):
    """
    Sinc function implementation.

    sinc(x) = sin(pi*x) / (pi*x), with sinc(0) defined as 1.

    Parameters:
        x (float): Input value.

    Returns:
        float: Output of sinc(x)
    """
    if x == 0:
        return 1.0
    return math.sin(math.pi * x) / (math.pi * x)


if __name__ == "__main__":
    # Example usage:
    for value in [-2, -1, 0, 1, 2]:
        print(f"sinc({value}) = {sinc(value)}")
