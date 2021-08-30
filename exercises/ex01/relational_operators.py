"""Relational Expressions for the cool kids!"""

__author__ = "730249177"

left: int = int(input("Left-hand side: "))
right: int = int(input("Right-hand side: "))
answer1: bool = left < right
answer2: bool = left >= right
answer3: bool = left == right
answer4: bool = left != right
print(str(left) + " < " + str(right) + " is " + str(answer1))
print(str(left) + " >= " + str(right) + " is " + str(answer2))
print(str(left) + " == " + str(right) + " is " + str(answer3))
print(str(left) + " != " + str(right) + " is " + str(answer4))