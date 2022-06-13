"""
Number guessing game

-- Ask the user to stake a bet
-- Generate a random number between 1 and 100
-- Ask the user to guess the number
-- If the user guesses the number, congratulate them
-- If the user guesses incorrectly, tell them if they guessed too high or too low
-- If the user guesses correctly return the amount that he user bet * 2.5 / guess count
-- If the user runs out of guesses, tell them they lost

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


def main():
    """
    Main function
    """

    max_guesses = 10
    guess_count = 0
    guess = 0

    message = (
        f"Welcome to the number guessing game!\n"
        f"You have {max_guesses} guesses to guess the number.\n"
        f"The computer will generate a random number between 1 and 100.\n"
        f"Try to guess it in as few attempts as possible."
    )
    print(message)

    bet = ask_user_to_stake_bet()
    number = generate_number()

    # Loop until the user guesses the number or runs out of guesses
    while guess != number and guess_count < max_guesses:
        guess = int(input("Take a guess: "))
        guess_count += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print("You guessed correctly!")
            print("You won $" + str(round((bet * 2.5) / guess_count)) + "!")

    # If the user runs out of guesses, tell them they lost
    if guess_count == max_guesses:
        print("You lost!")
        print("The number was " + str(number))


if __name__ == '__main__':
    main()
    input("Press Enter to exit.")
    exit()
