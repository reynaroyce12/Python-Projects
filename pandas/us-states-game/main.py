from turtle import *
import pandas


screen = Screen()
screen.title("US state guessing game")
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle = Turtle()
turtle.shape(image)

guessed_state = []
missed_states = []
guessed_number = 0


while len(guessed_state) <= 50:
    user_input = screen.textinput(title=f"{guessed_number}/50 guessed right", prompt="Next state?")

    data = pandas.read_csv('50_states.csv', engine='c', encoding='latin-1')

    states_list = data['state'].to_list()
    format_user_input = user_input[0].upper() + user_input[1:]
    # print(format_user_input)

    if format_user_input in states_list:
        draw = Turtle()
        draw.penup()
        draw.hideturtle()
        current_state = data[format_user_input == data.state]
        draw.goto(int(current_state.x), int(current_state.y))
        draw.write(format_user_input)
        guessed_number += 1
        guessed_state.append(format_user_input)

    elif user_input == 'exit':
        for states in states_list:
            if states not in guessed_state:
                missed_states.append(states)
        missed_data = pandas.DataFrame(missed_states)
        missed_data.to_csv("Missed_states.csv")
        break

    else:
        print("The guess is wrong! Check the spelling or try another!")

screen.exitonclick()
