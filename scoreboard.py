import subprocess
from customtkinter import CTkImage
from conect import connect_to_db
import customtkinter as ctk
from prettytable import PrettyTable
from center import center_window
from PIL import Image, ImageTk

def get_data():
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT username, score FROM accounts;"
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def display_table(data):
    sorted_data = sorted(data, key=lambda x: x[1], reverse=True)  # Ordenar por la segunda columna (score)
    table = PrettyTable(["Username", "Score"])
    for row in sorted_data:
        table.add_row(row)
    return table.get_string()

def show_table():
    data = get_data()
    table_content = display_table(data)
    table_label.configure(text=table_content)

def score_screen():
    # Configuración de la ventana principal
    score_app = ctk.CTk()
    score_app.title("Tabla de Puntajes")
    center_window(score_app, 500, 400)

    ctk.CTkLabel(score_app, text="Scoreboard", font=("Helvetica", 30)).pack(pady=20)

    # Crear un label para mostrar la tabla
    global table_label
    table_label = ctk.CTkLabel(score_app, text="", font=("Courier", 25), pady=10)
    table_label.pack()

    show_table()

    back_button = ctk.CTkButton(score_app, text="Regresar", command=lambda: [score_app.destroy()], fg_color="#00adb5", hover_color="#f05454", width=20, height=20)
    back_button.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

    # Iniciar la aplicación
    score_app.mainloop()