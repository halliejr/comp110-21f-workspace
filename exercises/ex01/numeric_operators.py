"""Numeric Operators for Smart Peeps."""

__author__ = "730249177"

left: int = int(input("Left-hand side: "))
right: int = int(input("Right-hand side: "))
answer1: int = left ** right
answer2: float = left / right
answer3: int = left // right
answer4: int = left % right
print(str(left) + " ** " + str(right) + " is " + str(answer1))
print(str(left) + " / " + str(right) + " is " + str(answer2))
print(str(left) + " // " + str(right) + " is " + str(answer3))
print(str(left) + " % " + str(right) + " is " + str(answer4))