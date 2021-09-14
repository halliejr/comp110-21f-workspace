"""Repeating a beat in a loop."""

__author__ = "730249177"

user_string: str = input("What beat do you want me to repeat?")
number: int = int(input("How many times do you want me to repeat it?"))
string: str = " " + user_string

if number > 0:
    while number > 0:
        number = number - 1
        user_string = user_string + string
    print(user_string)
else: 
    print("No beat...")