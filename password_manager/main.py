from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- CONSTANTS AND GLOBAL VARIABLES ------------------------------- #
CANVAS_WIDTH = 200
CANVAS_HEIGHT = 200
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
DARK = "#222831"
YELLOW = "#ffd369"
FONT_NAME = "Courier"

password = []


def validate():
    website = website_entry.get()
    email = email_entry.get()

    if len(website) == 0 or len(email) == 0:
        messagebox.showerror(title="Enter details!!", message="Please fill the details.")
        return False
    else:
        return True


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    # Password Generator Project
    global password
    password.clear()
    if validate():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                   'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        nr_letters = random.randint(4, 6)
        nr_symbols = random.randint(1, 2)
        nr_numbers = random.randint(1, 2)

        for num in range(nr_letters):
            random_char = random.choice(letters)
            password += random_char

        for num in range(nr_numbers):
            random_number = random.choice(numbers)
            password += random_number

        for num in range(nr_symbols):
            random_symbol = random.choice(symbols)
            password += random_symbol

        random.shuffle(password)
        password_str = "".join(password)
        password_entry.insert(0, password_str)
        pyperclip.copy(password_str)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if validate() or len(password) == 0:
        messagebox.showerror(title="Enter details!!", message="Please fill the details.")

    else:
        response = messagebox.askokcancel(title=website,
                                          message=f"These are the details entered\nEmail: {email}\nPassword: {password}"
                                                  f"\nIs it ok to save?")
        if response:
            with open("password_data.txt", mode="a") as file:
                newline = f"{website} | {email} | {password}\n"
                file.write(newline)
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=DARK)

canvas = Canvas(width=200, height=200, bg=DARK)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg=DARK, fg="white")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")
website_entry.focus()

email_label = Label(text="Email/Username:", bg=DARK, fg="white")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")
email_entry.insert(0, "huzefachabukswar@gmail.com")

password_label = Label(text="Password:", bg=DARK, fg="white")
password_label.grid(column=0, row=3)

password_entry = Entry(width=30)
password_entry.grid(column=1, row=3, sticky="W")

password_button = Button(text="Generate Password", bg=DARK, fg="white", command=generate_password)
password_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", width=36, bg=DARK, fg="white", command=add_password)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
