from tkinter import *
from tkinter import messagebox
from random import *
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for i in range(randint(1, 20))]
    password_symbols = [choice(symbols) for i in range(randint(1, 10))]
    password_numbers = [choice(numbers) for i in range(randint(1, 9))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVING PASSWORD ------------------------------- #

def save_details():
    website = website_entry.get()
    email_username = user_name_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Nothing should be left empty!")
    else:
        is_ok = messagebox.askokcancel(title="Password Manager",
                                       message=f"The details entered are email: {email_username}"
                                               f"\npassword: {password}\nSave this into the file?")
        if is_ok:
            with open('deets.txt', mode='a') as dataFile:
                dataFile.write(f"{website} | email: {email_username} | password: {password}\n")
                website_entry.delete(0, END)
                user_name_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
# window.minsize(width=600, height=600)
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=("Arial", 10, "normal"))
website_label.grid(column=0, row=1)
website_entry = Entry(width="35")
website_entry.focus()

website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

user_name = Label(text="Email/Username:", font=("Arial", 10, "normal"))
user_name.grid(column=0, row=2)
user_name_entry = Entry(width=35)
user_name_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

password_label = Label(text="Password:", font=("Arial", 10, "normal"))
password_label.grid(column=0, row=3)
password_entry = Entry(width=20)
password_entry.grid(column=1, row=3, sticky="EW")

generate_password_button = Button(text="Generate Password", font=("Arial", 10, "normal"), command=generate_password)
generate_password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", font=("Arial", 10, "normal"), width=35, command=save_details)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
