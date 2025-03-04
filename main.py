from utils import create_window
import tkinter as tk
import ttkbootstrap as ttk

def button_func():
    print('Button press')

window = create_window('test', '600x500')

# create ttk label widget
label = ttk.Label(master=window, text='test123')
label.pack()

# create text widget
text = tk.Text(master=window)
text.pack()

# create ttk entry widget
entry = ttk.Entry(master=window)
entry.pack()

# add label
label2 = ttk.Label(master=window, text='my label')
label2.pack()

# create ttk button
button = ttk.Button(master=window, text='Button A', command=button_func)
button.pack()

# create button
button2 = ttk.Button(master=window, text='Button2', command=lambda: print('hello'))
button2.pack()

window.mainloop()