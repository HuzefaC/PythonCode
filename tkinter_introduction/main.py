import tkinter

window = tkinter.Tk()
window.minsize(width=500, height=500)
my_label = tkinter.Label(text="Label", font=("Arial", 24))
my_label.pack()
window.mainloop()
