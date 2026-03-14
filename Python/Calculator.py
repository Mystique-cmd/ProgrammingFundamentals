import tkinter as tk
import re
import math

history = []  

memory_index = 0

calculated = False

def on_key_press(event):
    global calculated
    if calculated:
        entry.delete(0, tk.END)
        calculated = False

def insert_char(char):
    global calculated
    if calculated:
        entry.delete(0, tk.END)
        calculated = False
    entry.insert(tk.END, char)

def calculate():
    global calculated
    try:
        expression = entry.get()
        expression = expression.replace('^', '**')
        expression = re.sub(r'√(\d+(\.\d+)?)', r'math.sqrt(\1)', expression) 
        expression = re.sub(r'(\d+)%', r'(\1 / 100)', expression)
        expression = re.sub(r'(\d+(\.\d+)?)%', r'(\1/100)', expression)


        result = eval(expression)
        entry.insert(tk.END, f" = {result}")
        calculated = True
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "ERROR")
        calculated = True

def store_in_memory():
    content = entry.get()
    if "=" in content:
        try:
            history.append(content.strip())
            entry.delete(0, tk.END)
            entry.insert(tk.END, "STORED IN MEMORY")
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, f"ERROR STORING: {e}")
    else:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "NO RESULT TO STORE")

def recall_from_memory():
    global memory_index
    if history:
        entry.delete(0, tk.END)
        entry.insert(0, history[memory_index])
        memory_index = (memory_index + 1) % len(history)
    else:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "NO MEMORY STORED")

def clear_memory():
    history.clear()
    entry.delete(0, tk.END)
    entry.insert(tk.END, "MEMORY CLEARED")

root = tk.Tk()
root.title("Mystique's Calculator")
root.geometry("496x500")
root.configure(bg= "black")
root.resizable(False, False)  

entry = tk.Entry(root, width=31, font=('Arial', 20), bg='green')
entry.grid(row=0, column=0, columnspan=4, padx=10, ipady=20, pady=(20, 10))
entry.bind('<KeyPress>', on_key_press)

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
        button = tk.Button(root, text=text, command=lambda t=text: insert_char(t), width=5, height=2)
        button.grid(row=row, column=col)

exit_button = tk.Button(root, text='Exit', command=root.destroy, width=5, height=2, bg='red')
exit_button.grid(row=5, column=3, )

store = tk.Button(root, text='M+',command = store_in_memory, width=5, height=2, bg='yellow')
store.grid(row=5, column=0)

recall = tk.Button(root, text='MR', command=recall_from_memory, width=5, height=2, bg='yellow')
recall.grid(row=5, column=1)    

clear = tk.Button(root, text='MC', command=clear_memory , width=5, height=2, bg='yellow')
clear.grid(row=5, column=2)

pwr = tk.Button(root, text='^', command=lambda: insert_char('^'), width=5, height=2, bg='lightgreen')
pwr.grid(row=6, column=0)

sqrt = tk.Button(root, text='√', command=lambda: insert_char('√'), width=5, height=2, bg='lightgreen')
sqrt.grid(row=6, column=1)

per = tk.Button(root, text='%', command=lambda: insert_char('%'), width=5, height=2, bg='lightgreen')
per.grid(row=6, column=2)

root.mainloop()  # Start the main event loop