from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
DARK = "#222831"
YELLOW = "#ffd369"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=DARK)
# window.minsize(width=700, height=500)

canvas = Canvas(window, bg=DARK, height=224, width=200, highlightthickness=0)
filename = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=filename)
canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 34, "bold"))
canvas.grid(column=1, row=1)

timer_heading_label = Label(text="Timer", fg=GREEN, bg=DARK, font=(FONT_NAME, 40, "bold"))
timer_heading_label.grid(column=1, row=0)

start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), bg=GREEN)
stop_button = Button(text="Stop", font=(FONT_NAME, 10, "bold"), bg=GREEN)

start_button.grid(row=2, column=0)
stop_button.grid(row=2, column=2)

check_label = Label(text="✔", font=(FONT_NAME, 10, "bold"), fg=GREEN, bg=DARK)
check_label.grid(row=3, column=1)

window.mainloop()
