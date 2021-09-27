"""List utility functions."""

__author__ = "123456789"


# TODO: Implement your functions here.


def main() -> None:
    """Import Numbers for List."""
    print(all([1, 2, 1], 1))
    print(is_equal([1, 1], [1, 1]))
    print(max([1, 2, 3]))
    return None 


def all(x: list[int], y: int) -> bool:
    """All will return a bool indicating True or False."""
    start_len: int = len(x)
    i: int = 0
    h: bool = True
    while i < start_len:
        if x[i] != y:
            return False
        i += 1       
    else: 
        return h


def is_equal(x: list[int], y: list[int]) -> bool:
    """See if list values are equal."""
    i: int = 0
    h: bool = False
    if len(x) == len(y):
        while i < len(x):
            if x[i] == y[i]:
                return True
            i += 1
    else:
        return h


def max(input: list[int]) -> int:
    """Return the maximum number in the list."""
    i: int = 1
    j: int = input[0]
    if len(input) == 0:
        raise ValueError("max() arg is an empty list") 
    else:
        if input[i] != j:
            while input[i] >= j:
                return input[i]
            i += 1  
        return j

    
if __name__ == "__main__":
    main()