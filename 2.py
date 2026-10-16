import tkinter as tk

def on_button_click():
    label.config(text="Сәлем, Java!")

root = tk.Tk()
root.title("Тапсырма 2: Батырма әрекеті")
root.geometry("300x150")

btn = tk.Button(root, text="Басу", command=on_button_click, font=("Arial", 12))
btn.pack(pady=20)

label = tk.Label(root, text="", font=("Arial", 14), fg="red")
label.pack(pady=10)

root.mainloop()
