from tkinter import *

window = Tk()
window.title("Body Mass Index Calculator")
window.minsize(width = 260, height = 250)
window.config(padx = 20, pady = 20)

weight_label = Label(text = "Enter Your Weight (kg)", font = ("Arial", 12, "normal"), pady = 10)
weight_label.pack()
weight_entry = Entry(width = 30)
weight_entry.pack()

height_label = Label(text = "Enter Your Height (cm)", font = ("Arial", 12, "normal"), pady = 10)
height_label.pack()
height_entry = Entry(width = 30)
height_entry.pack()


def calculate_bmi():
    weight = weight_entry.get()
    height = height_entry.get()
    bmi = float(weight) / (float(height) / 100) ** 2
    if weight == "" or height == "":
        result_label.config(text="Enter your weight and height")
    else:
        try:
            bmi = float(weight) / ((float(height) / 100) ** 2)
            result_string = write_result(bmi)
            result_label.config(text=result_string)
        except:
            result_label.config(text="Enter a valid number!")

empty_label = Label()
empty_label.pack()

calculate_button = Button(text = "Calculate", command = calculate_bmi)
calculate_button.pack()

result_label = Label(pady = 20)
result_label.pack()


def write_result(bmi):
    result_string = f"Your BMI is {round(bmi, 1)} and you are "
    if bmi <= 16:
        result_string += "severely thin!"
    elif 16 < bmi <= 17:
        result_string += "moderately thin!"
    elif 17 < bmi <= 18.5:
        result_string += "mild thin!"
    elif 18.5 < bmi <= 25:
        result_string += "normal weight"
    elif 25 < bmi <= 30:
        result_string += "overweight"
    elif 30 < bmi <= 35:
        result_string += "obese"
    elif 35 < bmi:
        result_string += "extremely obese"
    return result_string


window.mainloop()