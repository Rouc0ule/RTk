import tkinter as tk
from gtk_button import RTkButton

def clicked():
    print('Clicked !')

root = tk.Tk()
root.configure(bg='black')

button = RTkButton(root, click_effect=None, command=clicked)
button.place(relx=0.5, rely=0.5, anchor='center')

root.mainloop()