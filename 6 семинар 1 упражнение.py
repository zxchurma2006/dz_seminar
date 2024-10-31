import tkinter as tk
def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        result_label.config(text=f"Результат: {result}")
    except Exception as e:
        result_label.config(text="Ошибка!")
root = tk.Tk()
root.title("Калькулятор")
entry = tk.Entry(root, width=40)
entry.pack(pady=20)
calc_button = tk.Button(root, text="Посчитать", command=calculate)
calc_button.pack(pady=10)
result_label = tk.Label(root, text="")
result_label.pack(pady=20)
root.mainloop()