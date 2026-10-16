import tkinter as tk

counter = 0
running = False

def update_timer():
    global counter, running
    if running:
        counter += 1
        time_label.config(text=f"Уақыт: {counter} сек")
        root.after(1000, update_timer)

def start_timer():
    global running
    if not running:
        running = True
        update_timer()

def stop_timer():
    global running
    running = False

root = tk.Tk()
root.title("Тапсырма 7: Таймер")
root.geometry("300x200")

time_label = tk.Label(root, text="Уақыт: 0 сек", font=("Arial", 16))
time_label.pack(pady=20)

btn_start = tk.Button(root, text="Бастау", width=10, command=start_timer)
btn_start.pack(pady=5)

btn_stop = tk.Button(root, text="Тоқтату", width=10, command=stop_timer)
btn_stop.pack(pady=5)

root.mainloop()
