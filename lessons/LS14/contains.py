"""Example of a function that processes a list."""

# Define a function named contains
# We can give two arguments: a needle value were searching for in a haystack.


def main() -> None:
    names: list[str] = ["Hallie", "Louis"]
    print(contains("Hallie", names))


def contains(needle: str, haystack: list[str]) -> bool:
    """Return True if needle is found in haystack, f]False otherwise."""
    # Loop throigh each item in list 
    i: int = 0
    while i < len(haystack): 
        if haystack[i] == needle:
            # Test if item stored at index is equal to needle 
            # Return true if so 
            return True
        i += 1
    # Return false after testing each item 
    return False

# Python Idiom for starting the main function
if __name__ == "__main__":
    main()