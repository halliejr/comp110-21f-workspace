"""List utility functions."""

__author__ = "123456789"


# TODO: Implement your functions here.


def main() -> None:
    """Import Numbers for List."""
    print(all([1, 1], 1))
    print(is_equal([1, 2], [2]))
    print(max([10, 5, 200, 20]))
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
    if len(x) != len(y):
        return False 
    else:
        while i < len(x):
            if x[i] != y[i]:
                return False
            else:
                i += 1
    return h


def max(input: list[int]) -> int:
    """Return the maximum number in the list."""
    i: int = 0
    start_len: int = len(input)
    if len(input) == 0:
        raise ValueError("max() arg is an empty list") 
    max: int = input[0]
    while i < start_len:
        if input[i] > max:
            max = input[i]
        i += 1 
    return max

    
if __name__ == "__main__":
    main()