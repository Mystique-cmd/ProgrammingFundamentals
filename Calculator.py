import tkinter as tk

#function to evaluate the  user input. The function does the following:
# 1. It uses eval() to calculate the result of the expression entered in the entry widget.
# 2. If the evaluation is successful, it clears the entry widget and inserts the result.
# 3. If an error occurs (e.g., invalid input), it clears the entry widget and displays "Error".
def calculate():
    try:
        result = eval(entry.get()) 
        entry.delete(0, tk.END)  
        entry.insert(tk.END, result)
    except Exception:
        entry.delete(0, tk.END)  
        entry.insert(tk.END, "Error")  

# Create the main window
root = tk.Tk()
root.title("Mystique's Calculator")
root.geometry("496x500")
root.configure(bg= "black")
root.resizable(False, False)  

# Create an entry widget for user input
entry = tk.Entry(root, width=31, font=('Arial', 20), bg='green')
entry.grid(row=0, column=0, columnspan=4, padx=10, ipady=20, pady=(20, 10))

# Create buttons for digits and operations
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), 
]
btn = tk.Button(root, text='=',command=calculate, width=5, height=2)
btn.grid(row=4, column=3)

for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, command=calculate, width=5, height=2)
    else:
        button = tk.Button(root, text=text, command=lambda t=text: entry.insert(tk.END, t), width=5, height=2)
        button.grid(row=row, column=col)
    
# Add an "Exit" button to close the program
    exit_button = tk.Button(root, text='Exit', command=root.destroy, width=5, height=2, bg='red', fg='white')
    exit_button.grid(row=5, column=1, columnspan=2, sticky='we', padx=10, pady=10)
root.mainloop()  # Start the main event loop
