"""Challenge Question #2!"""


def a(x: int) -> int:
    """A functions."""
    x = x // 2
    if x == 1:
        return 0
    else:
        return 1


def b(x: int) -> int:
    """Antoher function."""
    x = a(x + 1)
    return x


x: int = 2
print(b(x))