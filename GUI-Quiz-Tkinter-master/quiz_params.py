import tkinter as tk
from tkinter import messagebox

def button_click():
    
    try:
        
        input_text = input_field.get()
        input_number = number_field.get()
        global no_questions 
        no_questions= int(input_number)
        global category
        category = input_text
        print("You entered:", category, "and the number", no_questions)
        root.destroy()
    except ValueError:
         messagebox.showerror("Error", "Enter a number!")

root = tk.Tk()
root.title("String and Number Input Window")

input_label = tk.Label(root, text="Enter a string:")
input_label.pack()

input_field = tk.Entry(root, width=50)
input_field.pack()

number_label = tk.Label(root, text="Enter a number:")
number_label.pack()

number_field = tk.Entry(root, width=50)
number_field.pack()

button = tk.Button(root, text="Submit", command=button_click)
button.pack()

root.mainloop()
