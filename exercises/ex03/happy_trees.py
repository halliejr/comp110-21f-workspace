"""Drawing forests in a loop."""

__author__ = "730249177"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

space1: str = "" + TREE
depth: int = int(input("Depth: "))

if depth > 0:
    print(TREE)
    while depth > 1:
        depth = depth - 1
        TREE = TREE + space1
        print(TREE)
else:
    print(" ")