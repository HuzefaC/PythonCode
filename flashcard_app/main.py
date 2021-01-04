import pandas
from tkinter import *
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
FONTTITLE = ("Ariel", 40, "italic")
FONTWORD = ("Ariel", 60, "bold")

current_card = {}
word_dict = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("data/french_words.csv")
    word_dict = data.to_dict(orient="records")
else:
    word_dict = data.to_dict(orient="records")


def is_known():
    word_dict.remove(current_card)
    df = pandas.DataFrame(word_dict)
    df.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------- Flip ------------------------------- #
def card_flip():
    canvas.itemconfig(card, image=card_back_image)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=f"{current_card['English']}", fill="white")


# ---------------------------- Read CSV ------------------------------- #
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(word_dict)
    canvas.itemconfig(card, image=card_front_image)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=f"{current_card['French']}", fill="black")
    flip_timer = window.after(3000, func=card_flip)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("FlashCards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=card_flip)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400, 150, text="French", font=FONTTITLE)
card_word = canvas.create_text(400, 263, text="Word", font=FONTWORD)
canvas.grid(column=0, row=0, columnspan=2)

cross_image = PhotoImage(file="images/wrong.png")
cross_button = Button(image=cross_image, highlightthickness=0, command=next_card)
cross_button.grid(row=1, column=0)

check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command=is_known)
check_button.grid(row=1, column=1)

next_card()
window.mainloop()
