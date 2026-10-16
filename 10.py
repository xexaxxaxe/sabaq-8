import tkinter as tk

def submit_form():
    name = entry_name.get()
    age = entry_age.get()
    info_label.config(text=f"Аты: {name}, Жасы: {age}")

root = tk.Tk()
root.title("Тапсырма 10: Форма")
root.geometry("300x250")

tk.Label(root, text="Аты-жөні:").pack(pady=2)
entry_name = tk.Entry(root, width=20)
entry_name.pack(pady=2)

tk.Label(root, text="Жасы:").pack(pady=2)
entry_age = tk.Entry(root, width=20)
entry_age.pack(pady=2)

btn_submit = tk.Button(root, text="Жіберу", command=submit_form)
btn_submit.pack(pady=10)

info_label = tk.Label(root, text="", font=("Arial", 12), fg="dark green")
info_label.pack(pady=10)

root.mainloop()
