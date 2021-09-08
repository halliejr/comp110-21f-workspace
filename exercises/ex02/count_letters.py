"""Counting letters in a string."""

__author__ = "730249177"

# Begin your solution here...
user_string: str = input("What letter do you want me to search for?: ")
word: str = input("Enter a word: ")
count: int = 0
i: str = input(print("a"))
for i in user_string:
    if i == 'a':
        count = count + 1
while count < len(user_string):
    print(user_string[count])
else:
    print("Count: " + str(count))