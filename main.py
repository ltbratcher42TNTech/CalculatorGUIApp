import tkinter as tk

calculation = ""    # Initializing as an empty string

# This function adds a symbol to the expression the user is inputting
# It updates the calculation string and updated the display
def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

# Function to evaluate the calculation and show the result
def evaluate_calculation():
    global calculation
    try:
        result = str(eval(calculation))    # Evaluate using eval()
        calculation = ""    # Reset calculation string after evaluating
        text_result.delete(1.0, "end")    # Clear the expression
        text_result.insert(1.0, result)    # Display the result
    except:
        clear_field()   # If there's an error (e.g., invalid input), clear the field
        text_result.insert(1.0, "Error")    # Then display "Error"

# Function to clear the current calculation and result
def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")

# Initialize the main window for the app, including window title and window size
root = tk.Tk()
root.title("Calculator GUI App")
root.geometry("300x275")

# Create a text area for displaying the calculation and result, place it on a grid spanning 5 columns
text_result = tk.Text(root, height=2, width=16, font=("Arial", 24))
text_result.grid(columnspan=5)


# Create buttons for digits 1 to 9
btn_1 = tk.Button(root, text="1", command=lambda: add_to_calculation(1), width=5, font=("Arial", 14))
btn_1.grid(row=2, column=1)
btn_2 = tk.Button(root, text="2", command=lambda: add_to_calculation(2), width=5, font=("Arial", 14))
btn_2.grid(row=2, column=2)
btn_3 = tk.Button(root, text="3", command=lambda: add_to_calculation(3), width=5, font=("Arial", 14))
btn_3.grid(row=2, column=3)
btn_4 = tk.Button(root, text="4", command=lambda: add_to_calculation(4), width=5, font=("Arial", 14))
btn_4.grid(row=3, column=1)
btn_5 = tk.Button(root, text="5", command=lambda: add_to_calculation(5), width=5, font=("Arial", 14))
btn_5.grid(row=3, column=2)
btn_6 = tk.Button(root, text="6", command=lambda: add_to_calculation(6), width=5, font=("Arial", 14))
btn_6.grid(row=3, column=3)
btn_7 = tk.Button(root, text="7", command=lambda: add_to_calculation(7), width=5, font=("Arial", 14))
btn_7.grid(row=4, column=1)
btn_8 = tk.Button(root, text="8", command=lambda: add_to_calculation(8), width=5, font=("Arial", 14))
btn_8.grid(row=4, column=2)
btn_9 = tk.Button(root, text="9", command=lambda: add_to_calculation(9), width=5, font=("Arial", 14))
btn_9.grid(row=4, column=3)

# Creating button for number 0
btn_0 = tk.Button(root, text="0", command=lambda: add_to_calculation(0), width=5, font=("Arial", 14))
btn_0.grid(row=5, column=2)

# Create buttons for operators (+, -, *, /)
btn_plus = tk.Button(root, text="+", command=lambda: add_to_calculation("+"), width=5, font=("Arial", 14))
btn_plus.grid(row=2, column=4)
btn_minus = tk.Button(root, text="-", command=lambda: add_to_calculation("-"), width=5, font=("Arial", 14))
btn_minus.grid(row=3, column=4)
btn_mult = tk.Button(root, text="*", command=lambda: add_to_calculation("*"), width=5, font=("Arial", 14))
btn_mult.grid(row=4, column=4)
btn_div = tk.Button(root, text="/", command=lambda: add_to_calculation("/"), width=5, font=("Arial", 14))
btn_div.grid(row=5, column=4)

# Create buttons for parentheses
btn_openpar = tk.Button(root, text="(", command=lambda: add_to_calculation("("), width=5, font=("Arial", 14))
btn_openpar.grid(row=5, column=1)
btn_closepar = tk.Button(root, text=")", command=lambda: add_to_calculation(")"), width=5, font=("Arial", 14))
btn_closepar.grid(row=5, column=3)

# Create the "Clear" button
btn_clear = tk.Button(root, text="C", command=clear_field, width=11, font=("Arial", 14))
btn_clear.grid(row=6, column=1, columnspan=2)

# Create the "=" button
btn_equals = tk.Button(root, text="=", command=evaluate_calculation, width=11, font=("Arial", 14))
btn_equals.grid(row=6, column=3, columnspan=2)

# Start the GUI event loop
root.mainloop()
