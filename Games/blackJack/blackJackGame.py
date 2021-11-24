import random
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_sum(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    game_over = False

    for i in range(2):
        newu_card = deal_card()
        user_cards.append(newu_card)
        newc_card = deal_card()
        computer_cards.append(newc_card)

    while not game_over:
        user_score = calculate_sum(user_cards)
        computer_score = calculate_sum(computer_cards)
        print(f"User's cards are {user_cards} and score is {user_score}")
        print(f"Computer's card is {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
            print("You lose!")
            print("------------bye bye-----------")
        else:
            choice = input("Do you want to continue, type y or n \n").lower()
            if choice == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True
                if user_score > computer_score:
                    print("You win!!")
                elif computer_score == user_score:
                    print("It's a draw!")
                elif user_score == 21 and computer_score < 21:
                    print("Wooohooo you win with a black Jack!!")
                else:
                    print("You lose!!")


play_game()
while input("Do you wanna go again \n") == 'y':
    print("\n")
    play_game()