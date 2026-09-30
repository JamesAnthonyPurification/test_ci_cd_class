def add(a: float | int, b: float | int) -> float | int:
    return a + b  # Return the sum to the caller.


def subtract(a: float | int, b: float | int) -> float | int:
    return a - b  # Return the difference to the caller.


def multiply(a: float | int, b: float | int) -> float | int:
    return a * b  # Return the product to the caller.


def divide(a: float | int, b: float | int) -> float | int:
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b  # Return a floating-point quotient.


def power(base: float | int, exponent: int) -> float | int:
    if base == 0 and exponent < 0:
        raise ValueError("Zero cannot have a negative exponent.")
    return base ** exponent
