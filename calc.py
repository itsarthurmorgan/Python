



###########################     This code is only containg the box of the calculator not the buttons #####################################

import tkinter as tk

def evaluate_expression():
    expression = entry.get()
    try:
        result = eval(expression)
        result_label.config(text="Result: " + str(result))
    except:
        result_label.config(text="Invalid expression")

# Create the main window
window = tk.Tk()
window.title("Expression Calculator")

# Create an entry field for the expression
entry = tk.Entry(window)
entry.pack()

# Create a button to evaluate the expression
evaluate_button = tk.Button(window, text="Evaluate", command=evaluate_expression)
evaluate_button.pack()

# Create a label to display the result
result_label = tk.Label(window, text="Result: ")
result_label.pack()

# Start the main loop
window.mainloop()
