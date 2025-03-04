from utils import *
import tkinter as tk
import ttkbootstrap as ttk

def convert():
    try:
        mile_input = float(entry_var.get())
        km_output = mile_input * 1.61
        output_string.set(f"{km_output:.2f}km")
    except ValueError:
        output_string.set("Invalid input")

# create main window
window = create_window('Distance Converter', '400x150')

# title
title_label = ttk.Label(
    master=window,
    text='Distance Conversion',
    font='Arial 22 bold'
)
title_label.pack()

# input field
input_frame = ttk.Frame(master=window)
entry_var = tk.StringVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_var)
button = ttk.Button(
    master=input_frame,
    text='Convert',
    command=convert
)
entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=1)

# output
output_string = tk.StringVar()
output_label = ttk.Label(
    master=window,
    text='Output',
    font='Arial 22',
    textvariable=output_string
)
output_label.pack(pady=10)

# run
window.mainloop()