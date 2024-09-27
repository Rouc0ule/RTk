import tkinter as tk
from gtk_canvas import GTkCanvas

root = tk.Tk()

canvas = GTkCanvas(root, bg='red')
canvas.pack()
canvas.roundedRectangle(5, 5, 200, 100, fill='lightblue')

root.mainloop()