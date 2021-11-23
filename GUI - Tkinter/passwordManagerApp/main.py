from tkinter import *
from tkinter import messagebox
from random import *
import json
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(1, 20))]
    password_symbols = [choice(symbols) for _ in range(randint(1, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(1, 9))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ------------------------------- SEARCHING FOR WEBSITE --------------------------

def check_item():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")


# ---------------------------- SAVING PASSWORD ------------------------------- #

def save_details():

    website = website_entry.get()
    email = user_name_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Nothing should be left empty!")
    else:
        try:
            with open('data.json', 'r') as dataFile:
                data = json.load(dataFile)
        except FileNotFoundError:
            with open('data.json', 'w') as dataFile:
                json.dump(new_data, dataFile, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as dataFile:
                json.dump(data, dataFile, indent=4)
        finally:
            website_entry.delete(0, END)
            user_name_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(120, 100, image=img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", font=("Arial", 10, "normal"))
website_label.grid(column=0, row=1)
website_entry = Entry(width=20)
website_entry.focus()
website_entry.grid(column=1, row=1, sticky="EW")

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

search_button = Button(text="Search", font=("Arial", 10, "normal"), command=check_item)
search_button.grid(column=2, row=1, sticky="EW")

window.mainloop()
