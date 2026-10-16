import tkinter as tk

def show_input():
    text = entry.get()
    output_label.config(text=f"Енгізілген мәтін: {text}")

root = tk.Tk()
root.title("Тапсырма 9: Мәтінді өңдеу")
root.geometry("300x200")

entry = tk.Entry(root, width=20, font=("Arial", 12))
entry.pack(pady=20)

btn = tk.Button(root, text="Көрсету", command=show_input)
btn.pack()

output_label = tk.Label(root, text="", font=("Arial", 12), fg="blue")
output_label.pack(pady=20)

root.mainloop()
