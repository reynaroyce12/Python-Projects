from tkinter import *
from tkinter import messagebox


# ------------------------------------- BMI CALCULATOR --------------------------------
def calculate_bmi():
    weight = int(weight_entry.get())
    height = int(height_entry.get())
    height_m = height / 100
    height_square = height_m * height_m
    if height > 300:
        messagebox.showwarning(title="Error!", message="Height should not be more than 300cm")
    else:
        bmi = round(weight / height_square, 2)
        text_label.config(text=f"Your BMI is {bmi}", font=("Courier", 15, "bold"))


# --------------------------------------UI SETUP --------------------------------------
window = Tk()
window.title("BMI Calculator")
window.config(padx=50, pady=30, bg="#C8E3D4")

canvas = Canvas(width=350, height=250, bg="#C8E3D4", highlightthickness=0)
img = PhotoImage(file="BMI_image1.png")
canvas.create_image(140, 120, image=img)
canvas.grid(row=1, column=2)

text_label = Label(text="Calculate your BMI",  font=("Courier", 15, "bold"), bg="#C8E3D4")
text_label.grid(row=2, column=1, columnspan=2, padx=0, pady=15)

weight_label = Label(text="Weight (kg)", font=("Courier", 10, "bold"), bg="#C8E3D4")
weight_label.grid(row=3, column=1)
weight_entry = Entry(width=20)
weight_entry.focus()
weight_entry.grid(row=3, column=2)

height_label = Label(text="Height (Cm)", font=("Courier", 10, "bold"), bg="#C8E3D4")
height_label.grid(row=4, column=1)
height_entry = Entry(width=20)
height_entry.grid(row=4, column=2)

calculate_button = Button(text="Calculate", font=("Courier", 10, "bold"), command=calculate_bmi)
calculate_button.grid(row=5, column=2, padx=0, pady=10)

window.mainloop()
