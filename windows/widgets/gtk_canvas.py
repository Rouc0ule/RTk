import tkinter as tk

class GTkCanvas(tk.Canvas):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def roundedRectangle(self, x, y, width, height, r=25, **kwargs):
        points = [x+r, y,
                x+r, y,
                x+width-r, y,
                x+width-r, y,
                x+width, y,
                x+width, y+r,
                x+width, y+r,
                x+width, y+height-r,
                x+width, y+height-r,
                x+width, y+height,
                x+width-r, y+height,
                x+width-r, y+height,
                x+r, y+height,
                x+r, y+height,
                x, y+height,
                x, y+height-r,
                x, y+height-r,
                x, y+r,
                x, y+r,
                x, y]
        self.create_polygon(points, **kwargs, smooth=True)