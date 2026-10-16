import tkinter as tk

root = tk.Tk()
root.title("Тапсырма 4: Графика")
root.geometry("400x250")

canvas = tk.Canvas(root, width=400, height=250, bg="white")
canvas.pack()

# Тікбұрыш (Қызыл)
canvas.create_rectangle(30, 50, 130, 110, fill="red")

# Шеңбер / Эллипс (Жасыл)
canvas.create_oval(160, 50, 240, 130, fill="green")

# Үшбұрыш (Көк)
canvas.create_polygon(320, 50, 270, 130, 370, 130, fill="blue")

root.mainloop()
