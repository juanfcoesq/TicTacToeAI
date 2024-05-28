import subprocess
import tkinter as tk
import customtkinter as ctk
from center import center_window
from conect import connect_to_db

def user_logged_in(username):
    print("Usuario ingresado:", username)
    get_user_id(username)

def get_user_id(username):
    conn = connect_to_db()
    cursor = conn.cursor()

    # Ejecutar una consulta SQL para buscar el ID del usuario basado en su nombre de usuario
    query = f"SELECT id FROM accounts WHERE username = '{username}';"
    cursor.execute(query)
    result = cursor.fetchone()  # Obtener el primer resultado de la consulta
    cursor.close()
    conn.close()

    global id
    if result:
        id = result[0]
    else:
        id = None

def configure_account(option, user_id):
    new_value = ""
    if option == "Username":
        new_value = username_entry.get()
        column_name = "username"
    elif option == "Password":
        new_value = password_entry.get()
        column_name = "password"
    else:
        print("Opción no válida")

    # Realizar la inserción en la base de datos
    if new_value:
        conn = connect_to_db()
        cursor = conn.cursor()
        query = f"UPDATE accounts SET {column_name} = '{new_value}' WHERE id = {user_id};"
        cursor.execute(query)
        conn.commit()
        cursor.close()
        conn.close()
        print(f"Nueva {option} configurada y guardada en la base de datos: {new_value}")

def config_screen():
    # Configuración de la ventana principal
    config_app = ctk.CTk()
    config_app.title("Configurar Cuenta")
    center_window(config_app, 500, 400)

    ctk.CTkLabel(config_app, text="Configuración", font=("Helvetica", 30)).pack(pady=30)

    # Etiqueta de instrucción
    instruction_label = ctk.CTkLabel(config_app, text="Seleccione lo que desea configurar:")
    instruction_label.pack(pady=5)

    # Opciones de configuración
    options_frame = ctk.CTkFrame(config_app)
    options_frame.pack(pady=5)

    username_button = ctk.CTkButton(options_frame, text="Usuario", command=lambda: configure_account("Username", id))
    username_button.pack(side=tk.LEFT, padx=5)

    password_button = ctk.CTkButton(options_frame, text="Contraseña", command=lambda: configure_account("Password", id))
    password_button.pack(side=tk.LEFT, padx=5)

    # Entradas de texto
    global username_entry, password_entry
    username_label = ctk.CTkLabel(config_app, text="Nuevo nombre de usuario:")
    username_label.pack()

    username_entry = ctk.CTkEntry(config_app)
    username_entry.pack()

    password_label = ctk.CTkLabel(config_app, text="Nueva contraseña:")
    password_label.pack()

    password_entry = ctk.CTkEntry(config_app, show="*")  # El texto en la entrada se mostrará como asteriscos (*)
    password_entry.pack()

    # Botón para salir de la aplicación
    exit_button = ctk.CTkButton(config_app, text="Salir", command=config_app.destroy)
    exit_button.pack(pady=30)

    # Iniciar la aplicación
    config_app.mainloop()
