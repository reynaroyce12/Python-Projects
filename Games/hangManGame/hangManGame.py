import random
from hangManWords import word_list
from hangManArts import logo, stages

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

display = []
for letter in range(len(chosen_word)):
    display += "_"

lives = 6
end_of_game = False

while not end_of_game:
    guess = input("Enter your guess: ").lower()

    if guess in display:
        print("You've already entered that.Try another one!")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = guess

    if guess not in chosen_word:
        print("You guessed a letter which is not in the word.You lost a life")

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    print(stages[lives])
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win!")

