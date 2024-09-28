import customtkinter as ctk
import tkinter as tk

root = ctk.CTk()

canvas = ctk.CTkCanvas(root, height=20, width=20)
canvas.pack()
canvas.create_aa_circle(10, 10, 5, fill='blue')

tkcanvas = tk.Canvas(root, height=20, width=20)
tkcanvas.pack()
tkcanvas.create_oval(10, 10, 20, 20, fill='blue')

button = ctk.CTkButton(root)
button.pack()

root.mainloop()