from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
card = {}

# ----------------------------------- FILE MECHANISM -----------------------------
data = pandas.read_csv('./data/french_words.csv')
data_dict = data.to_dict(orient='records')


def check():
    global card, timer
    window.after_cancel(timer)
    card = random.choice(data_dict)
    french_word = card['French']
    canvas.itemconfig(title, text="French", fill='black')
    canvas.itemconfig(word, text=french_word, fill='black')
    canvas.itemconfig(card_bg, image=img_front)
    timer = window.after(3000, func=change_card)


def change_card():
    english_trans = card['English']
    canvas.itemconfig(title, text="English", fill='white')
    canvas.itemconfig(word, text=english_trans, fill='white')
    canvas.itemconfig(card_bg, image=img_back)


# --------------------------------- UI SETUP -----------------------------------

window = Tk()
window.title("Flash Card Application")
window.config(padx=30, pady=30, bg=BACKGROUND_COLOR)
timer = window.after(3000, func=change_card)

canvas = Canvas(width=900, height=550, bg=BACKGROUND_COLOR, highlightthickness=0)
img_front = PhotoImage(file="./images/card_front.png")
img_back = PhotoImage(file="./images/card_back.png")
card_bg = canvas.create_image(450, 275, image=img_front)
title = canvas.create_text(450, 120, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(450, 265, text="", font=("Ariel", 50, "bold"))
canvas.grid(row=1, column=1, columnspan=2)

cross_image = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=cross_image, highlightthickness=0, command=check)
wrong_button.grid(row=2, column=1)

right_image = PhotoImage(file="./images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=check)
right_button.grid(row=2, column=2)

check()

window.mainloop()
