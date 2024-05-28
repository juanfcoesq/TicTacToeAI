import customtkinter as ctk
from tkinter import messagebox
import mysql.connector
from conect import connect_to_db
from center import  center_window

def add_user_to_db(username, password):
    conn = connect_to_db()
    if conn is None:
        print("Conexión a la base de datos fallida")  # Mensaje de depuración
        return False

    if validar_existencia(username):
        try:
            cursor = conn.cursor()
            query = "INSERT INTO accounts (username, password) VALUES (%s, %s)"
            cursor.execute(query, (username, password))
            conn.commit()
            print("Usuario agregado correctamente")  # Mensaje de depuración
            return True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False
        finally:
            cursor.close()
            conn.close()
    else:
        messagebox.showerror("Error", "Usuario ya existente, usa otro nickname")

def add_user_screen():
    add_app = ctk.CTk()
    add_app.title("Agregar Usuario")
    center_window(add_app, 500, 400)
    ctk.CTkLabel(add_app, text="Registrar Usuario", font=("Helvetica", 30)).pack(pady=20)

    label_username = ctk.CTkLabel(add_app, text="Nombre de usuario:", font=("Helvetica", 20))
    label_username.pack(pady=10)

    entry_username = ctk.CTkEntry(add_app)

    entry_username.pack(pady=5)

    label_password = ctk.CTkLabel(add_app, text="Contraseña:", font=("Helvetica", 20))
    label_password.pack(pady=10)

    entry_password = ctk.CTkEntry(add_app, show="*")
    entry_password.pack(pady=5)

    add_button = ctk.CTkButton(add_app, text="Agregar", command=lambda: handle_add_user(entry_username.get(), entry_password.get()))
    add_button.pack(pady=20)

    add_app.mainloop()

def handle_add_user(username, password):
    if add_user_to_db(username, password):
        messagebox.showinfo("Éxito", "Usuario agregado correctamente")
    else:
        messagebox.showerror("Error", "No se pudo agregar el usuario")


def validar_existencia(username):
    conn = connect_to_db()
    cursor = conn.cursor()
    query = "SELECT * FROM accounts WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()

    if result is None:
        print("Usuario no encontrado")  # Mensaje de depuración
        return True
    else:
        return False