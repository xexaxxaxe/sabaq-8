import tkinter as tk

root = tk.Tk()
root.title("Тапсырма 1: Мәтін шығару")
root.geometry("300x150")

label = tk.Label(root, text="Зертханалық жұмыс №10", fg="blue", font=("Arial", 16, "bold"))
label.pack(pady=40)

root.mainloop()
