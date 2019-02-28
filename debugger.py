
import tkinter as tk



#setup graphical debugger
root = tk.Tk()
root.geometry("500x500")
canvas = tk.Canvas(root, width="550", height="550")
canvas.pack()
canvas.create_rectangle(0,0,50,50, fill="red")

root.mainloop()