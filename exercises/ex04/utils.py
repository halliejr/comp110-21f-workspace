"""List utility functions."""

__author__ = "123456789"


# TODO: Implement your functions here.


def main() -> None:
    """Import Numbers for List."""
    print(all([1, 1, 1], 1))
    print(is_equal([1, 0, 1], [1, 1, 1]))
    print(max([100, 99, 101]))
    return None 


def all(x: list[int], y: int) -> bool:
    """All will return a bool indicating True or False."""
    start_len: int = len(x)
    i: int = 0
    h: bool = True
    while i < start_len:
        if x[i] == y:
            return h
        i += 1       
    else: 
        return False


def is_equal(x: list[int], y: list[int]):
    """See if list values are equal."""
    list_leny: int = len(y)
    i: int = 0
    h: bool = True
    while i < list_leny:
        if x[i] == y:
            return h
        i += 1
    else:
        return False


def max(input: list[int]) -> int:
    """Return the maximum number in the list."""
    i: int = 0
    j: int = 101
    if len(input) != 0:
        while input[i] <= 1:
            return j
    else:
        raise ValueError("max() arg is an empt list")
    return j


if __name__ == "__main__":
    main()