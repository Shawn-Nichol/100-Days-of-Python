import random
import art

def difficulty_level():
    """Select the difficulty level of the game. """
    play_type = "invalid"
    while play_type == "invalid":
        play_type = input("Do you want to play easier or hard: 'e' for easy 'h' for hard?\n").lower()

        if play_type == "e":
            print("Easy game mode, activated")
            return 10
        elif play_type == "h":
            print("Hard game mode, activated")
            return 5
        else:
            play_type = "invalid"
            print("Please enter an a valid play type")
    return 0


def guess_number(num_guesses, ran_num):
    """
    Guess the number
    :param num_guesses: how many guess the users has
    :param ran_num: random number chosen
    :return:
    """
    while num_guesses > 0:
        print(f"You have {num_guesses} guesses left")
        number_guess = int(input("Select number: \n"))
        if number_guess > ran_num:
            print(f"{number_guess} is too high")
        elif number_guess < ran_num:
            print(f"{number_guess} is too low")
        else:
            print(f"{ran_num}: you guess correctly")
            break
        num_guesses -= 1

    print(f"game over you ran out of guesses, the correct number was {ran_num}")

print(art.logo)
print("Welcome to Number guessing")

continue_playing = True
while continue_playing:
    guess_number(difficulty_level(), random.randint(1,100))

    if input("Do you want to play again Y/N").upper() == "N":
        continue_playing = False
        print("Thank you for playing, goodbye!")




