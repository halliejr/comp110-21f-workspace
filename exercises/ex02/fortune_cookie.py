"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730249177"
from random import randint

print("Your fortune cookie says...")
choice = randint(1, 100)
if choice < 50:
    print("An old love will come back to you in the coming days.")
else: 
    if choice <= 30:
        print("The specific thing that you have wished for will come true.")
    else:
        if choice <= 10:
            print("Life is about to be better than it has ever been for you.")
        else: 
            print("A fresh start will put you on your way.")
print("Now, go spread positive vibes!")