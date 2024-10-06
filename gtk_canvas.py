import tkinter as tk

class GTkCanvas(tk.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(borderwidth=0, highlightthickness=0, *args, **kwargs)
