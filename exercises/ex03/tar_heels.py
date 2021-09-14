"""An exercise in remainders and boolean logic."""

__author__ = "730249177"


number: int = int(input("Enter an int:"))

if ((number % 2) == 0) and ((number % 7) == 0):
    # number is divisible by 2 and 7
    print("TAR HEELS")
else:
    if (number % 2) == 0:
        # number is divisible by 7
        print("TAR")
    else:
        if (number % 7) == 0:
            # number is divisible by 7
            print("HEELS")                      
        else:
            # number is not divisible by 2 or 7
            print("CAROLINA")