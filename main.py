from tkinter import *


def calculater_button():
    try:

        y = height_entry.get()
        x = weight_entry.get()
        calculation = float(x) / (float(y) / 100 * float(y) / 100)
        if calculation < 18.5:
            our_label.config(text="Under Weight")
        elif 18.5 <= calculation < 24.9:
            our_label.config(text="Normal Weight")
        elif 24.9 <= calculation < 29.9:
            our_label.config(text="Over Weight")
        elif 29.9 <= calculation < 34.9:
            our_label.config(text="Obesity Class 1")
        elif 34.9 <= calculation < 39.9:
            our_label.config(text="Obesity Class 2")
        elif 40 < calculation:
            our_label.config(text="Obesity Class 3")
    except ValueError:
        if x == "" or y == "":
            our_label.config(text="Enter both weight and height")
        else:
            our_label.config(text="Enter a valid number")


window = Tk()
window.title("BMI Calculater")
window.minsize(height=300, width=300)

weight_label = Label(text="Enter Your Weight (kg)", pady=8)
weight_label.pack()

weight_entry = Entry(width=13)
weight_entry.pack()

height_label = Label(text="Enter Your Height (cm)", pady=8)
height_label.pack()

height_entry = Entry(width=13)
height_entry.pack()

button = Button(text="Calculate", command=calculater_button)
button.pack()

our_label = Label()
our_label.pack()

mainloop()
