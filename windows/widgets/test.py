from gtk_canvas import *

root = tk.Tk()

canvas = GTkCanvas(root, width=150, height=100)
canvas.pack()
canvas.roundedRectangle(0, 0, 150, 100)

root.mainloop()