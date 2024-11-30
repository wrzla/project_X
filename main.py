import tkinter as tk

# Создаем главное окно
root = tk.Tk()
root.title("Создатель")
root.geometry("400x200") 

# Создаем кнопки
button1 = tk.Button(root, text="ZOV1", command=lambda: open_second_window(), width=15)
button1.pack(pady=10)

button2 = tk.Button(root, text="ZOV2", command=lambda: print("Нажата ZOV2"), width=15)
button2.pack(pady=10)

button3 = tk.Button(root, text="ZOV3", command=lambda: print("Нажата ZOV3"), width=15)
button3.pack(pady=10)

# Функция для открытия второго окна
def open_second_window():
    # Создаем второе окно
    second_window = tk.Toplevel(root)
    second_window.title("Ввод данных")
    second_window.geometry("400x200")  # Устанавливаем размер второго окна 

    # Добавляем поля ввода
    fio_label = tk.Label(second_window, text="ФИО:")
    fio_label.pack()
    fio_entry = tk.Entry(second_window)
    fio_entry.pack()

    year_label = tk.Label(second_window, text="Год рождения:")
    year_label.pack()
    year_entry = tk.Entry(second_window)
    year_entry.pack()

    birthplace_label = tk.Label(second_window, text="Место рождения:")
    birthplace_label.pack()
    birthplace_entry = tk.Entry(second_window)
    birthplace_entry.pack()

    # Добавляем поля для увлечений и спорта
    hobbies_label = tk.Label(second_window, text="Увлечения:")
    hobbies_label.pack()
    hobbies_entry = tk.Entry(second_window)
    hobbies_entry.pack()

    sport_label = tk.Label(second_window, text="Занимаетесь ли вы спортом?")
    sport_label.pack()
    sport_var = tk.StringVar(value="нет")  # По умолчанию "нет"
    sport_radio_yes = tk.Radiobutton(second_window, text="Да", variable=sport_var, value="да")
    sport_radio_yes.pack()
    sport_radio_no = tk.Radiobutton(second_window, text="Нет", variable=sport_var, value="нет")
    sport_radio_no.pack()

    # Добавляем место для фотографии
    photo_label = tk.Label(second_window, text="Фото:")
    photo_label.pack()
    # Здесь можно добавить функциональность для загрузки изображения

    # Запускаем второе окно
    second_window.mainloop()

# Запускаем главное окно
root.mainloop()