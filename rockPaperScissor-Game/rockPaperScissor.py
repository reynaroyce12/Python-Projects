import random


def checking():
    play_again = input("Do you wanna play again? Type 'y' for yes and 'n' for no \n").lower()
    if play_again == 'y':
        print("\n")
        playgame()
    elif play_again == 'n':
        print("-----bye byee-----")
    else:
        print("Enter something valid!")


def playgame():
    items = ["Rock", "Paper", "Scissor"]
    # user input part
    user_selected = int(input("What do you choose? Enter 0 for Rock, 1 for Paper and 2 for scissors: \n"))

    if items[user_selected] == "Rock":
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)
              (____)
        ---.__(___)
        """)
    elif items[user_selected] == "Paper":
        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)
    else:
        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)

    print('\n')

    # computer generating part

    random_num = random.randint(0, 2)

    if random_num == 0:
        print("Computer Chose Rock: ")
        print("""
            _______
        ---'   ____)
              (_____)
              (_____)1
              (____)
        ---.__(___)
        """)
    elif random_num == 1:
        print("Computer Chose Paper: ")
        print("""
             _______
        ---'    ____)____
                   ______)
                  _______)
                 _______)
        ---.__________)
        """)
    else:
        print("Computer Chose Scissors: ")
        print("""
            _______
        ---'   ____)____
                  ______)
               __________)
              (____)
        ---.__(___)
        """)

    # result part
    # including few exceptions too
    if user_selected == 0 and random_num == 2:
        print("Yaaayy! You won!")
        checking()
    elif user_selected == 1 and random_num == 2:
        print("Oops! You lose!")
        checking()
    elif user_selected == 2 and random_num == 1:
        print("Yaaayy! You won!")
        checking()
    elif user_selected > random_num:
        print("Oops! You lose!")
        checking()
    elif user_selected < random_num:
        print("Yaaayy! You won!")
        checking()
    elif user_selected == random_num:
        print("Draw!")
        checking()
    else:
        print("Invalid Choice!")
        checking()


playgame()
