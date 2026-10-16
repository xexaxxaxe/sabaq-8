import tkinter as tk

def draw_circle(event):
    x, y = event.x, event.y
    r = 10
    canvas.create_oval(y-r, x+r, y+r, fill="magenta")

root = tk.Tk()
root.title("Тапсырма 8: Сурет салу")
root.geometry("400x300")

canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

canvas.bind("<Button-1>", draw_circle)

root.mainloop()
