import tkinter as tk
from tkinter import ttk
import psycopg2

def refresh_table():
    for string in table.get_children():
        table.delete(string)

def show_alkan():
    with psycopg2.connect(
            host="127.0.0.1",  # адрес
            dbname="alcohols_task5",  # название бд
            user="postgres",  # имя пользователя бд
            password="1111",  # пароль от бд
            port="5432"
    ) as con:
        with con.cursor() as cur:
            cur.execute("""
                SELECT name, formula, carbon_count, hydrogen_count, molar_mass
                FROM public.alcohols 
                ORDER BY carbon_count ASC
            """, )
            alkanes = cur.fetchall()

    refresh_table()

    for alkan in alkanes:
        name = alkan[0]
        formula = alkan[1]
        carbon_count = alkan[2]
        hydro_count = alkan[3]
        molar_mass = alkan[4]
        table.insert("", tk.END, values=(name, formula, carbon_count, hydro_count, molar_mass))

win = tk.Tk()
win.title("Спирты — органическая химия")
win.geometry("680x420")

lbl = ttk.Label(win, text="Каталог спиртов")
lbl.pack(pady=10)

show_btn = ttk.Button(win, text="Показать", command=show_alkan)
show_btn.pack(pady=5)

refresg_btn = ttk.Button(win, text="Очистить таблицу", command=refresh_table)
refresg_btn.pack(pady=5)

table = ttk.Treeview(win, columns=("name", "formula", "carbon_count", "hydrogen_count", "molar_mass"), show="headings", height = 3)

table.heading("name", text="Название")
table.heading("formula", text="Формула")
table.heading("carbon_count", text="Атомов углерода")
table.heading("hydrogen_count", text="Атомов водорода")
table.heading("molar_mass", text="Молярная масса")


table.pack(padx=15, pady=10, fill="both", expand=False)

scrl = ttk.Scrollbar(win, orient="vertical", command=table.yview)
scrl.pack(side="right", fill="y", pady=50)

show_alkan()

win.mainloop()