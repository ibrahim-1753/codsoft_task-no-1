import tkinter as tk
from tkinter import messagebox

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = num1 / num2

        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numbers.")
    except ZeroDivisionError as e:
        messagebox.showerror("Math Error", str(e))

#Initialize the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x250")
root.resizable(False, False)

#First number input
label1 = tk.Label(root, text="First Number:")
label1.pack(pady=5)
entry1 = tk.Entry(root, width=20)
entry1.pack(pady=5)

#Second number input
label2 = tk.Label(root, text="Second Number:")
label2.pack(pady=5)
entry2 = tk.Entry(root, width=20)
entry2.pack(pady=5)

#Buttons for operations
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="+", width=8, command=lambda: calculate('add'))
add_button.grid(row=0, column=0, padx=5)

subtract_button = tk.Button(button_frame, text="-", width=8, command=lambda: calculate('subtract'))
subtract_button.grid(row=0, column=1, padx=5)

multiply_button = tk.Button(button_frame, text="*", width=8, command=lambda: calculate('multiply'))
multiply_button.grid(row=1, column=0, padx=5)

divide_button = tk.Button(button_frame, text="/", width=8, command=lambda: calculate('divide'))
divide_button.grid(row=1, column=1, padx=5)

#Result display
result_label = tk.Label(root, text="Result: ", font=("Arial", 14))
result_label.pack(pady=20)

root.mainloop()