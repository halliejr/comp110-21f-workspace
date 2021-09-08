"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730249177"
from random import randint

choice = randint(1, 100)
if choice < 50:
    print("Your fortune cookie says...")
    print("An old love will come back to you in the coming days.")
    print("Now, go spread positive vibes!")
else: 
    if choice <= 30:
        print("Your fortune cookie says...")
        print("The specific thing that you have wished for will come true.")
        print("Now, go spread positive vibes!")
    else:
        if choice <= 10:
            print("Your fortune cookie says...")
            print("Life is about to be better than it has ever been for you.")
            print("Now, go spread positive vibes!")
        else: 
            if choice <= 5:
                print("Your fortune cookie says...")
                print("Life is what you make it.")
                print("Now, go spread positive vibes!")
            else:
                print("Your fortune cookie says...")
                print("You will be rewarded for all of your hard work.")
                print("Now, go spread positive vibes!")