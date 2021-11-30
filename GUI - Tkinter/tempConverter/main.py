from tkinter import *
# from tkinter import messagebox

BG_COLOR = '#F2DDC1'
CANVAS_COLOR = '#E2C2B9'
TEXT_COLOR = '#66806A'


# ------------------------------------ CONVERSIONS AND RESETS -----------------------------------

def convert_f():
    fahrenheit = float(f_entry.get())

    celsius1 = round(5 / 9 * (fahrenheit - 32), 2)
    c_entry.insert(0, celsius1)

    kelvin1 = round(273.15 + ((fahrenheit - 32) * (5 / 9)), 2)
    k_entry.insert(0, kelvin1)


def convert_c():
    celsius = float(c_entry.get())

    fahrenheit1 = round((celsius * 9 / 5) + 32, 2)
    f_entry.insert(0, fahrenheit1)

    kelvin2 = round(celsius + 273.15, 2)
    k_entry.insert(0, kelvin2)


def convert_k():
    kelvin = float(k_entry.get())

    celsius2 = round(kelvin - 273.15)
    c_entry.insert(0, celsius2)

    fahrenheit2 = round(9 / 5 * (kelvin - 273.15) + 32)
    f_entry.insert(0, fahrenheit2)


def reset_all():
    f_entry.delete(0, END)
    c_entry.delete(0, END)
    k_entry.delete(0, END)


# ------------------------------------- UI SETUP --------------------------------

window = Tk()
window.title("Temperature Converter 🌡️")
window.config(padx=30, pady=30, bg=BG_COLOR)

img_canvas = Canvas(width=350, height=310, bg=BG_COLOR, highlightthickness=0)
img = PhotoImage(file='thermometer-icon.png')
img_canvas.create_image(190, 150, image=img)
img_canvas.grid(row=1, column=2)

text_canvas = Canvas(width=320, height=210, bg=CANVAS_COLOR, highlightthickness=3, highlightbackground='black')
text_canvas.create_text(80, 22, text="Fahrenheit: ", font=("Courier", 12, "bold"), fill=TEXT_COLOR)
text_canvas.create_text(68, 62, text="Celsius: ", font=("Courier", 12, "bold"), fill=TEXT_COLOR)
text_canvas.create_text(65, 104, text="Kelvin: ", font=("Courier", 12, "bold"), fill=TEXT_COLOR)
text_canvas.create_text(210, 22, text="°F", font=("Courier", 13, "bold"), fill=TEXT_COLOR)
text_canvas.create_text(210, 64, text="°C", font=("Courier", 13, "bold"), fill=TEXT_COLOR)
text_canvas.create_text(210, 105, text="°K", font=("Courier", 13, "bold"), fill=TEXT_COLOR)
text_canvas.grid(row=2, column=2)

f_entry = Entry(width=10)
f_window = text_canvas.create_window(130, 13, anchor=NW, window=f_entry)
f_entry.focus()

c_entry = Entry(width=10)
c_window = text_canvas.create_window(130, 53, anchor=NW, window=c_entry)

k_entry = Entry(width=10)
k_window = text_canvas.create_window(130, 94, anchor=NW, window=k_entry)

f_button = Button(text="Convert", font=("Courier", 10, "bold"), command=convert_f)
f_button = text_canvas.create_window(240, 10, anchor=NW, window=f_button)

c_button = Button(text="Convert", font=("Courier", 10, "bold"), command=convert_c)
c_button = text_canvas.create_window(240, 50, anchor=NW, window=c_button)

k_button = Button(text="Convert", font=("Courier", 10, "bold"), command=convert_k)
k_button = text_canvas.create_window(240, 90, anchor=NW, window=k_button)

reset_button = Button(text="RESET", font=("Courier", 12, "bold"), command=reset_all)
reset_button = text_canvas.create_window(130, 150, anchor=NW, window=reset_button)

window.mainloop()
