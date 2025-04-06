import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import io
import contextlib
import os
import platform

# Импортируем bootstrap для настройки sys.path
import bootstrap

# Импортируем функции ETL и инициализации БД из интерфейса
from interface import run_init_db, run_extract, run_transform, run_load, run_reset, run_all

def run_command(command_func):
    """
    Запускает переданную функцию, перенаправляя вывод в текстовое поле.
    """
    output = io.StringIO()
    with contextlib.redirect_stdout(output):
        command_func()
    result = output.getvalue()
    text_widget.insert(tk.END, result + "\n")
    text_widget.see(tk.END)

def clear_console():
    """
    Очищает текстовое окно логов и терминал.
    """
    # Очищаем текстовое окно
    text_widget.delete("1.0", tk.END)
    # Очищаем терминал (работает в командной строке)
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

# Создаем основное окно приложения
root = tk.Tk()
root.title("Sales Analysis ETL Desktop App")
root.geometry("800x500")

# Фрейм для кнопок
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Кнопки для выполнения команд ETL
btn_init = tk.Button(button_frame, text="Инициализация БД", width=20, command=lambda: run_command(run_init_db))
btn_init.grid(row=0, column=0, padx=5, pady=5)

btn_extract = tk.Button(button_frame, text="Извлечь данные", width=20, command=lambda: run_command(run_extract))
btn_extract.grid(row=0, column=1, padx=5, pady=5)

btn_transform = tk.Button(button_frame, text="Преобразовать данные", width=20, command=lambda: run_command(run_transform))
btn_transform.grid(row=0, column=2, padx=5, pady=5)

btn_load = tk.Button(button_frame, text="Загрузить данные", width=20, command=lambda: run_command(run_load))
btn_load.grid(row=1, column=0, padx=5, pady=5)

btn_reset = tk.Button(button_frame, text="Сброс БД", width=20, command=lambda: run_command(run_reset))
btn_reset.grid(row=1, column=1, padx=5, pady=5)

btn_all = tk.Button(button_frame, text="Полный ETL", width=20, command=lambda: run_command(run_all))
btn_all.grid(row=1, column=2, padx=5, pady=5)

# Кнопка для очистки логов
btn_clear = tk.Button(button_frame, text="Очистить логи", width=20, command=clear_console)
btn_clear.grid(row=2, column=1, padx=5, pady=5)

# Текстовое поле для вывода результатов работы команд
text_widget = ScrolledText(root, width=90, height=20)
text_widget.pack(padx=10, pady=10)

# Запуск приложения
root.mainloop()
