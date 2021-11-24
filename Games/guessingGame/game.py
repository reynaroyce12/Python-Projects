import random
from art import logo

print(logo)


def checking():
    if user_num < random_num:
        print("Too low!")
    elif user_num > random_num:
        print("Too high!")
    else:
        print("Woohoo you guessed it right!")


def level_checking():
    user_choice = input("Choose a difficulty level 'easy' or 'hard': ").lower()
    if user_choice == 'easy':
        return attempts_easy
    elif user_choice == 'hard':
        return attempts_hard
    else:
        print("Invalid choice!")


attempts_easy = 10
attempts_hard = 5

print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")

random_num = random.randint(1, 100)
# print(random_num)

game_over = False

turns = level_checking()
print(f"You have {turns} attempts left to guess the number")

while not game_over:
    user_num = int(input("Go on, make a guess: "))
    checking()
    if user_num == random_num:
        break
    else:
        turns -= 1
    print(f"You have {turns} left")
    if turns == 0:
        print("You have no attempts left! You lose")
        print(f"The right number was {random_num}")
        game_over = True

