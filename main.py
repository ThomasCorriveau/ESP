import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=3)

# instructions
instructions = tk.Label(root, text="Yo", font="Arial")
instructions.grid(columnspan=3, column=0, row=1)


root.mainloop()

#yo
