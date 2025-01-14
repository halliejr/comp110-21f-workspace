"""S-CARD to Death!"""

__author__ = "730249177"

player: str
points: int = 1
continue_playing: bool = True
CLUB: str = '\u2663'
SPADES: str = '\u2660'
DIAMOND: str = '\u2666'
HEART: str = '\u2665'
BLACK_HEART: str = '\u2764\uFE0F'


def main() -> None:
    """The program's entrypoint."""
    greet()
    global points 
    global continue_playing 
    while continue_playing:
        option1: int = int(input("Do you want to guess the color of a card " + player + "? 1 = Yes and 2 = No: "))
        if option1 == 1:
            points = points + 5
            color()
        else:
            option2: int = int(input(player + ", do you want to guess the number on the card? 1 = Yes or 2 = No: "))
            if option2 == 1:
                points = points + 5
                number(points)
            else:
                option3: int = int(input("Do you wish to end the game " + player + "? 1 = Yes or 2 = No: "))
                if option3 == 1:
                    points = points + 1
                    continue_playing = False
                    print("The game has ended game and you will now receieve 10 years of bad luck. Thank you for playing S-CARD to Death! You have earned " + str(points) + " adventure points. " + BLACK_HEART)
                else:
                    points = points + 5
                    color()   
    return None


def greet() -> None:
    """Greeting the player."""
    global player
    player = input("Enter your name: ")
    print(player + " are you ready to play S-CARD to Death? " + CLUB + SPADES + DIAMOND + HEART)
    print("About this game. A very smart, talented, beautiful individual invented this game you are about to play, called S-CARD to Death. Here are the instructions for the game. You will choose a card from the stack. Now, I must inform you that the cards in this stack may be cursed. Be very careful of your guesses, as they could lead to XDANGERX! Continue playing to see how many adventure points you can earn! ") 
    return None


def color() -> None:
    """The color of the card is Red."""
    global points
    global player 
    global continue_playing
    response1 = int(input("Pick a color; 1 = Red, 2 = Black: "))
    if response1 == 1:
        points = points + 5
        suit: int = int(input("Nice job " + player + "! You have earned 5 points. Now, guess the suit of the card. 1 = Hearts, 2 = Spades, 3 = Clubs, 4 = Diamonds. "))
        from random import randint
        e = randint(1, 4)
        if suit > 0:
            while e > suit:
                points = points + 5
                e = e - 1
            print(f"Good work {player}! You have earned 5 points. Final question. ")
            number(points)
    else:
        points = points + 1
        print("Sorry! That answer was incorrect. The game has ended and you will be single forever. Your total adventure points earned are " + str(points))
    keep_playing() 
    return None


def number(points: int) -> int:
    """The number on the card is lower than 6."""
    points = points
    global player 
    global continue_playing
    y: int = int(input("Guess if the number is higher or lower than 6: 1 = Higher, 2 = Lower: "))
    if y == 2:
        points = points + 5
        print("Wow " + player + ", you rock! You have earned 5 points. ")
        print("You have won the game " + player + " !!! Congratulations! " + CLUB + SPADES + HEART + DIAMOND + " Thank you for playing S-CARD to Death. Your total adventure points earned are " + str(points))
    else:
        points = points + 1
        print("Sorry! That answer was incorrect. The game has ended and you will be single forever. Your total adventure points earned are " + str(points))
    return points


def keep_playing() -> None:
    """Do you want to continue playing the game?"""
    global continue_playing 
    question1: int = int(input("Do you want to continue playing the game? 1 = Yes and 2 = No: "))
    if question1 == 1:
        main()
    else:
        continue_playing = False
        print("Goodbye. ")


if __name__ == "__main__":
    main()