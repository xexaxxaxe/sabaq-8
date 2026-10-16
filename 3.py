import tkinter as tk

def show_text():
    label.config(text="Salem!")

def hide_text():
    label.config(text="")

root = tk.Tk()
root.title("Тапсырма 3: Екі батырма")
root.geometry("300x150")

btn_show = tk.Button(root, text="Қосу", command=show_text)
btn_show.pack(side=tk.LEFT, padx=30, pady=20)

btn_hide = tk.Button(root, text="Өшіру", command=hide_text)
btn_hide.pack(side=tk.RIGHT, padx=30, pady=20)

label = tk.Label(root, text="", font=("Arial", 12))
label.pack(pady=10)

root.mainloop()
