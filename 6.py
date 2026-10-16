import tkinter as tk

def add_numbers():
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        result_label.config(text=f"Қосындысы: {n1 + n2}")
    except ValueError:
        result_label.config(text="Қате: Сан енгізіңіз!")

root = tk.Tk()
root.title("Тапсырма 6: Сандарды қосу")
root.geometry("300x200")

tk.Label(root, text="Сан 1:").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root, text="Сан 2:").pack()
entry2 = tk.Entry(root)
entry2.pack()

btn = tk.Button(root, text="Қосу", command=add_numbers)
btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
