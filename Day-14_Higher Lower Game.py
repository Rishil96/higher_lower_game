# Day 14 Project Higher Lower Game
import random
from HL_game_data import data

# Load data
game_data = data
data_count = len(game_data)


# Function to randomly select 2 data points from data
def give_choices():
    choice1 = random.randint(0, data_count - 1)
    choice2 = random.randint(0, data_count - 1)
    return game_data[choice1], game_data[choice2]


# Function to return celebrity with higher followers
def guess_checker(a, b):
    return a['name'] if a['follower_count'] > b['follower_count'] else b['name']


def play_higher_lower():
    print("Welcome to Higher Lower!")

    game_on = True
    score = 0

    while game_on:
        print(f"\nYour current score: {score}")
        choice_a, choice_b = give_choices()
        print(f"Choice A: {choice_a['name']}, a {choice_a['description']} from {choice_a['country']}")
        print('\t\tV.S.')
        print(f"Choice B: {choice_b['name']}, a {choice_b['description']} from {choice_b['country']}")

        # Take user guess to compare which data point has higher follower count
        guess = None
        while guess not in ['A', 'B']:
            guess = input("\nWho has more followers. Type A or B: ").upper()
            if guess not in ['A', 'B']:
                print("Invalid Guess. Choose A or B.")

        correct_celebrity = guess_checker(choice_a, choice_b)

        if guess == 'A':
            guessed_celebrity = choice_a['name']
        else:
            guessed_celebrity = choice_b['name']

        print(f"\nYour guess: {guessed_celebrity}")
        print(f"Correct answer: {correct_celebrity}")

        if guessed_celebrity == correct_celebrity:
            print("\nYou guessed correctly!")
            score += 1
        else:
            print("\nIncorrect Guess! You lose")
            print(f"\nYour final score is {score}")
            game_on = False

    play_again = input("\nDo you want to play again? Type y or n: ")

    if play_again == 'y':
        play_higher_lower()
    else:
        print("\nHave a nice day!")


play_higher_lower()
