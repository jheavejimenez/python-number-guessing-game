"""
Number guessing game

-- Ask the user to stake a bet
-- Generate a random number between 1 and 100
-- Ask the user to guess the number
-- If the user guesses the number, congratulate them
-- If the user guesses incorrectly, tell them if they guessed too high or too low
-- If the user guesses correctly return the amount they bet plus the amount they won

"""
import random


def generate_number():
    """
    Generate a random number between 1 and 100
    """
    return random.randint(1, 100)


def ask_user_to_stake_bet():
    """
    Ask the user to stake a bet
    """
    bet = int(input("How much would you like to bet? "))
    print("You have bet $" + str(bet) + ".")
    print("")
    return bet


