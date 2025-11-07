def step_function(x, threshold=0):
    """
    Step function.
    Returns 1 if x >= threshold, otherwise 0.

    Parameters:
        x (float): Input value.
        threshold (float): Step point (default 0).

    Returns:
        int: 1 or 0
    """
    return 1 if x >= threshold else 0


if __name__ == "__main__":
    # Example usage:
    for value in [-2, -1, 0, 1, 2]:
        print(f"step_function({value}) = {step_function(value)}")
