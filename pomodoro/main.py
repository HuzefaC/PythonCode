from tkinter import *
import math

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
reps = 0
my_timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(my_timer)
    timer_heading_label.config(text="Timer", fg=GREEN, bg=DARK, font=(FONT_NAME, 40, "bold"))
    canvas.itemconfig(timer_text, text="00:00")
    global reps
    reps = 0
    check_label.config(text="", font=(FONT_NAME, 10, "bold"), fg=GREEN, bg=DARK)


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time = LONG_BREAK_MIN * 60
    reps += 1
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        timer_heading_label.config(text="Work", fg=GREEN, bg=DARK, font=(FONT_NAME, 40, "bold"))
        count_down(work_time)
    elif reps == 2 or reps == 4 or reps == 6:
        timer_heading_label.config(text="Break", fg=PINK, bg=DARK, font=(FONT_NAME, 40, "bold"))
        count_down(short_break_time)
    elif reps == 8:
        timer_heading_label.config(text="Break", fg=RED, bg=DARK, font=(FONT_NAME, 40, "bold"))
        count_down(long_break_time)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"

    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global my_timer
        my_timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        global reps
        if reps == 2:
            check_label.config(text="✔", font=(FONT_NAME, 10, "bold"), fg=GREEN, bg=DARK)
        elif reps == 4:
            check_label.config(text="✔✔", font=(FONT_NAME, 10, "bold"), fg=GREEN, bg=DARK)
        elif reps == 6:
            check_label.config(text="✔✔✔", font=(FONT_NAME, 10, "bold"), fg=GREEN, bg=DARK)
        elif reps == 8:
            check_label.config(text="✔✔✔✔", font=(FONT_NAME, 10, "bold"), fg=GREEN, bg=DARK)
            reps = 0


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=DARK)
# window.minsize(width=700, height=500)

canvas = Canvas(window, bg=DARK, height=224, width=200, highlightthickness=0)
filename = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=filename)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 34, "bold"))
canvas.grid(column=1, row=1)

timer_heading_label = Label(text="Timer", fg=GREEN, bg=DARK, font=(FONT_NAME, 40, "bold"))
timer_heading_label.grid(column=1, row=0)

start_button = Button(text="Start", font=(FONT_NAME, 10, "bold"), bg=GREEN, command=start_timer)
stop_button = Button(text="Reset", font=(FONT_NAME, 10, "bold"), bg=GREEN, command=reset_timer)

start_button.grid(row=2, column=0)
stop_button.grid(row=2, column=2)

check_label = Label(font=(FONT_NAME, 10, "bold"), fg=GREEN, bg=DARK)
check_label.grid(row=3, column=1)
window.mainloop()
