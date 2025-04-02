#Scientific Calculator to calculate the square root, power, logarithm, and trigonometric functions.
# Importing the required libraries
import math
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

# Function to calculate the square root of a number
def calculate_square_root():    
    try:
        number = float(entry.get())
        if number < 0:
            raise ValueError("Negative number")
        result = math.sqrt(number)
        messagebox.showinfo("Result", f"The square root of {number} is {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid non-negative number.")

def calculate_power():
    try:
        base = float(entry.get())
        exponent = simpledialog.askfloat("Input", "Enter the exponent:")
        if exponent is None:
            return
        result = math.pow(base, exponent)
        messagebox.showinfo("Result", f"{base} raised to the power of {exponent} is {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def calculate_logarithm():
    try:
        number = float(entry.get())
        if number <= 0:
            raise ValueError("Non-positive number")
        result = math.log(number)
        messagebox.showinfo("Result", f"The logarithm of {number} is {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive number.")

def calculate_algorithm_base_10():
    try:
        number = float(entry.get())
        if number <= 0:
            raise ValueError("Non-positive number")
        result = math.log10(number)
        messagebox.showinfo("Result", f"The logarithm base 10 of {number} is {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive number.")

def calculate_sine():
    try:
        angle = float(entry.get())
        result = math.sin(math.radians(angle))
        messagebox.showinfo("Result", f"The sine of {angle} degrees is {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def calculate_cosine():
    try:
        angle = float(entry.get()) 
        result = math.cos(math.radians(angle))
        messagebox.showinfo("Result", f"The cosine of {angle} degrees is {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def calculate_tangent():
    try:
        angle = float(entry.get())
        result = math.tan(math.radians(angle))
        messagebox.showinfo("Result", f"The tangent of {angle} degrees is {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def calculate_arcsine():
    try:
        value = float(entry.get())
        if value < -1 or value > 1:
            raise ValueError("Out of range")
        result = math.degrees(math.asin(value))
        messagebox.showinfo("Result", f"The arcsine of {value} is {result} degrees")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number between -1 and 1.")

def calculate_arccosine():
    try:
        value = float(entry.get())
        if value < -1 or value > 1:
            raise ValueError("Out of range")
        result = math.degrees(math.acos(value))
        messagebox.showinfo("Result", f"The arccosine of {value} is {result} degrees")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number between -1 and 1.")

def calculate_arctangent():
    try:
        value = float(entry.get())
        result = math.degrees(math.atan(value))
        messagebox.showinfo("Result", f"The arctangent of {value} is {result} degrees")
    except ValueError:  
        messagebox.showerror("Error", "Please enter a valid number.")

def calculate_arctangent2():
    try:
        y = float(entry.get())
        x = simpledialog.askfloat("Input", "Enter the x coordinate:")
        if x is None:
            return
        result = math.degrees(math.atan2(y, x))
        messagebox.showinfo("Result", f"The arctangent of {y}/{x} is {result} degrees")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

# Function to clear the entry field
def clear_entry():
    entry.delete(0, tk.END)

# Function to exit the application
def exit_app():
    root.destroy()

# Creating the main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x400")
root.configure(bg="lightblue")
root.resizable(False, False)

# Creating the entry field
entry = tk.Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=20)
entry.focus_set()

# Creating the buttons
button_frame = tk.Frame(root, bg="lightblue")
button_frame.pack(pady=10)

buttons = [
    ("Square Root", calculate_square_root),
    ("Power", calculate_power),
    ("Logarithm", calculate_logarithm),
    ("Logarithm Base 10", calculate_algorithm_base_10),
    ("Sine", calculate_sine),
    ("Cosine", calculate_cosine),
    ("Tangent", calculate_tangent),
    ("Arcsine", calculate_arcsine),
    ("Arccosine", calculate_arccosine),
    ("Arctangent", calculate_arctangent),
    ("Arctangent2", calculate_arctangent2),
]

for (text, command) in buttons:
    button = tk.Button(button_frame, text=text, command=command, width=15, font=("Arial", 12), bg="lightgreen")
    button.pack(side=tk.LEFT, padx=5)

# Creating the clear and exit buttons
clear_button = tk.Button(root, text="Clear", command=clear_entry, width=10, font=("Arial", 12), bg="lightyellow")
clear_button.pack(pady=5)
exit_button = tk.Button(root, text="Exit", command=exit_app, width=10, font=("Arial", 12), bg="lightcoral")
exit_button.pack(pady=5)

# Running the main loop
root.mainloop()

# This code creates a simple GUI-based scientific calculator using Tkinter.
# It allows users to perform various calculations such as square root, power, logarithm, and trigonometric functions.
# The calculator also handles errors and provides user-friendly messages.
# The calculator is designed to be simple and easy to use, with a clear layout and responsive buttons.
# The calculator can be extended with additional features as needed.
# The code is well-structured and organized, making it easy to read and maintain.