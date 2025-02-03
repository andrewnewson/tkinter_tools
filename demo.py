import tkinter as tk
from tkinter import ttk

# create main window
window = tk.Tk()
window.title('Demo')
window.geometry('400x400')

# title
title_label = ttk.Label(master=window, text='Distance Conversion')
title_label.pack()

# run
window.mainloop()