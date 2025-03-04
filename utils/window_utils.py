import tkinter as tk
import ttkbootstrap as ttk

def create_window(title, size, theme='yeti'):
    window = ttk.Window(themename=theme)
    window.title(title)
    window.geometry(size)

    return window

