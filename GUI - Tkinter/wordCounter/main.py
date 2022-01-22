from tkinter import *


# ------------------------------ COUNT FUNCTION ----------------------

def count_word():
    content = entry_text.get("1.0", END)
    content_list = content.split()
    word_count = len(content_list)
    char_count = 0
    for word in content_list:
        if word != content_list[-1]:
            char_len = len(word) + 1
            char_count += char_len
        else:
            char_len = len(word)
            char_count += char_len
    count_label.config(text=f"{word_count} words {char_count} characters")


# -----------------------------UI SETUP ------------------------------

window = Tk()
window.title("Word Counter")
window.config(padx=30, pady=30, bg='#D6E5FA')

title_text = Label(text="WORD COUNTER", font=("Courier", 15, "bold"), bg='#D6E5FA')
title_text.grid(row=1, column=2, columnspan=2, pady=10)

entry_text = Text(width=75, height=20, borderwidth=3)
entry_text.grid(row=2, column=2, columnspan=2, pady=10)

button = Button(text="Count", font=("Courier", 15, "bold"), command=count_word)
button.grid(row=3, column=2, columnspan=2, pady=10)

count_label = Label(text="", font=("Courier", 12, "bold"), bg='#D6E5FA')
count_label.grid(row=4, column=2, columnspan=2)

window.mainloop()
