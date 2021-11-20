from tkinter import *

WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
show_time = None


# ---------------------------- TIMER MECHANISM ------------------------------- #

def reset():
    window.after_cancel(show_time)
    canvas.itemconfig(time_text, text="00:00")
    title.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0


def start_timer():
    global reps
    reps += 1

    work_secs = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        timer(long_break_sec)
        title.config(text="Break")
    elif reps % 2 == 0:
        timer(short_break_sec)
        title.config(text="5 min break!")
    else:
        timer(work_secs)
        title.config(text="Work work")


def timer(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(time_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global show_time
        show_time = window.after(1000, timer, count - 1)
    else:
        start_timer()
        marks = ""
        sessions = math.floor(reps / 2)
        for i in range(sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg="#FFF9B6")

title = Label(text="Timer", font=("Courier", 15, "bold"), fg="black", bg="#FFF9B6")
title.grid(column=1, row=0)

canvas = Canvas(width=200, height=225, bg="#FFF9B6", highlightthickness=0)
img = PhotoImage(file="./tomato.png")
canvas.create_image(100, 112, image=img)
time_text = canvas.create_text(103, 120, text="00:00", font=("Courier", 15, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", font=("Courier", 15, "bold"), command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", font=("Courier", 15, "bold"), command=reset)
reset_button.grid(column=3, row=3)

check_marks = Label(bg="#FFF9B6")
check_marks.grid(column=1, row="3")

window.mainloop()
