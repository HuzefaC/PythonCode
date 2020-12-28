from tkinter import *


def calculate():
    val = new_entry.get()
    val = round(int(val) * 1.61, 2)
    kms_value_label["text"] = val


# Creating a new window and configurations
window = Tk()
window.title("Widget Examples")
window.minsize(width=100, height=100)

new_entry = Entry(width=10)
new_entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

kms_value_label = Label(text="0")
kms_value_label.grid(column=1, row=1)

kms_label = Label(text="Km")
kms_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=calculate)
calculate_button.grid(column=1, row=2)


window.mainloop()
