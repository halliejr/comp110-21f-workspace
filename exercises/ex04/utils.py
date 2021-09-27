"""List utility functions."""

__author__ = "123456789"


# TODO: Implement your functions here.


def main() -> None:
    """Import Numbers for List."""
    print(all([1, 1], 1))
    print(is_equal([1, 2, 3], [4, 5, 6]))
    print(max([-1, -2, -3, 0]))
    return None 


def all(x: list[int], y: int) -> bool:
    """All will return a bool indicating True or False."""
    list_len: int = len(x)
    i: int = 0
    h: bool = True
    if list_len == 0:
        return False
    else:
        while i < list_len:
            if x[i] != y:
                return False
            i += 1      
        return h 
        

def is_equal(x: list[int], y: list[int]) -> bool:
    """See if list values are equal."""
    i: int = 0
    h: bool = True
    if (len(x) and len(y)) == 0:
        return h
    else:
        while len(x) == len(y):
            while i < len(x):
                if x[i] != y[i]:
                    return False
                else:
                    i += 1
        return h


def max(input: list[int]) -> int:
    """Return the maximum number in the list."""
    i: int = 0
    j: int = input[0]
    start_len: int = len(input)
    if len(input) == 0:
        raise ValueError("max() arg is an empty list") 
    else:
        if i < start_len:
            i += 1
            while input[i] <= j:
                return j
            i += 1 
        return input[i]

    
if __name__ == "__main__":
    main()