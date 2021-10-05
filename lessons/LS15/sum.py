"""Example of writing a test subject."""


# While loop
def sum(xs: list[float]) -> float:
    """Compute the sum of a list."""
    total: float = 0.0
    i: int = 0
    while i < len(xs):
        total += xs[i]
        i += 1
    return total 

# For...in loop


def sum1(xs: list[float]) -> float:
    """Compute the sum of a list."""
    total: float = 0.0
    for x in xs:
        total += x
    return total 