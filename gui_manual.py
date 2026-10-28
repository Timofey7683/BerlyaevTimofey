import tkinter as tk
from tkinter import ttk
import psycopg2

def refresh_table():
    for string in table.get_children():
        table.delete(string)

def show_alkan():
    with psycopg2.connect(
            host="127.0.0.1",  # адрес
            dbname="organ_chemistry",  # название бд
            user="postgres",  # имя пользователя бд
            password="1111",  # пароль от бд
            port="5432"
    ) as con:
        with con.cursor() as cur:
            cur.execute("""
                SELECT name, formula, carbon_count
                FROM public.alkanes 
                ORDER BY carbon_count ASC
            """, )
            alkanes = cur.fetchall()

    refresh_table()

    for alkan in alkanes:
        name = alkan[0]
        f = alkan[1]
        count_atom = alkan[2]
        table.insert("", tk.END, values=(name, f, count_atom))

win = tk.Tk()
win.title("Алканы — органическая химия")
win.geometry("680x420")

lbl = ttk.Label(win, text="Каталог алканов")
lbl.pack(pady=10)

show_btn = ttk.Button(win, text="Показать", command=show_alkan)
show_btn.pack(pady=5)

refresg_btn = ttk.Button(win, text="Очистить таблицу", command=refresh_table)
refresg_btn.pack(pady=5)

table = ttk.Treeview(win, columns=("name", "formula", "carbon_count"), show="headings", height=10)

table.heading("name", text="Название")
table.heading("formula", text="Формула")
table.heading("carbon_count", text="Атомов углерода")


table.pack(padx=15, pady=10, fill="both", expand=True)

#table.insert("", tk.END, values=("Метан", "CH4", 1))
#table.insert("", tk.END, values=("Этан", "C2H6", 2))
#table.insert("", tk.END, values=("Пропан", "C3H8", 3))

show_alkan()

win.mainloop()