import tkinter as tk

def change_color(selection):
    color_map = {"Ақ": "white", "Қызыл": "red", "Жасыл": "green", "Сары": "yellow"}
    root.config(bg=color_map.get(selection, "white"))

root = tk.Tk()
root.title("Тапсырма 5: Түс ауыстыру")
root.geometry("300x200")

selected_color = tk.StringVar(root)
selected_color.set("Ақ")

menu = tk.OptionMenu(root, selected_color, "Ақ", "Қызыл", "Жасыл", "Сары", command=change_color)
menu.pack(pady=40)

root.mainloop()
