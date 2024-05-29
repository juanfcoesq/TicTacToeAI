import subprocess
from conect import connect_to_db
import customtkinter as ctk
from prettytable import PrettyTable
from center import center_window

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
    score_app.configure(fg_color="#EEEEEE")

    ctk.CTkLabel(score_app, text="Scoreboard", font=("Helvetica", 30), text_color="#686D76").pack(pady=20)

    # Crear un label para mostrar la tabla
    global table_label
    table_label = ctk.CTkLabel(score_app, text="", font=("Courier", 25), pady=10, text_color="#686D76")
    table_label.pack()

    show_table()

    back_button = ctk.CTkButton(score_app, text="Regresar",command=lambda: [score_app.destroy()], text_color="#373A40", fg_color="#DC5F00", hover_color="#686D76")
    back_button.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

    # Iniciar la aplicación
    score_app.mainloop()