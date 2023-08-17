import tkinter as tk

def click_button(number):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + str(number))

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create an entry field for input
entry = tk.Entry(root, width=50,borderwidth=10,foreground="blue")
entry.grid(row=0, column=0, columnspan=4)

# Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

# Create and place buttons
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, padx=30, pady=30,bd=5,bg="white",fg="red", command=lambda t=text: button_click(t))
    button.grid(row=row, column=col)

# Button click function
def button_click(char):
    if char == '=':
        calculate()
    elif char == 'C':
        clear()
    else:
        click_button(char)

# Start the GUI event loop
root.mainloop()
