import customtkinter as ctk
from conect import connect_to_db
from center import center_window
from PIL import Image
from menu import menu
import config
import tablerojuego
import main_functions

def handle_login(username, password):
    print(f"Nombre de usuario ingresado: {username}")  # Mensaje de depuración
    print(f"Contraseña ingresada: {password}")  # Mensaje de depuración

    if login(username, password):
        return True
    else:
        return False

def login(username, password):
    global cursor
    conn = connect_to_db()
    if conn is None:
        print("Conexión a la base de datos fallida")  # Mensaje de depuración
        return False

    try:
        cursor = conn.cursor()
        query = "SELECT password FROM accounts WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()

        if result is None:
            print("Usuario no encontrado")  # Mensaje de depuración
            return False

        stored_password = result[0]

        if stored_password == password:
            print("Inicio de sesión exitoso")  # Mensaje de depuración
            return True
        else:
            print("Contraseña incorrecta")  # Mensaje de depuración
            return False

    finally:
        cursor.close()
        conn.close()

def login_screen():
    login_app = ctk.CTk()
    login_app.title("Login")
    center_window(login_app, 700, 600)

    ctk.CTkLabel(login_app, text="Log-In", font=("Helvetica", 50)).pack(pady=80)

    label_username = ctk.CTkLabel(login_app, text="Nombre de usuario:", font=("Helvetica", 30))
    label_username.pack(pady=10)

    entry_username = ctk.CTkEntry(login_app, width=300, height=30, placeholder_text="<USUARIO>")
    entry_username.pack(pady=5)

    label_password = ctk.CTkLabel(login_app, text="Contraseña:", font=("Helvetica", 30))
    label_password.pack(pady=10)

    entry_password = ctk.CTkEntry(login_app, show="*", width=300, height=30, placeholder_text="<PASSWORD>")
    entry_password.pack(pady=5)

    def attempt_login():
        # Lógica de autenticación
        if handle_login(entry_username.get(), entry_password.get()):  # Supongamos que la autenticación es exitosa
            config.user_logged_in(entry_username.get())
            tablerojuego.user_logged_in(entry_username.get())
            login_app.destroy()
            menu()
        else:
            ctk.CTkLabel(login_app, text="Usuario o contraseña incorrectos", font=("Helvetica", 20), fg_color="red").pack(pady=5)

    login_button = ctk.CTkButton(login_app, text="Log-in", command=attempt_login, fg_color="#00adb5", hover_color="#f05454", width=200, height=30, font=("Helvetica", 20))
    login_button.pack(pady=60)

    back_button = ctk.CTkButton(login_app, text="Regresar", command=lambda: [login_app.destroy(), main_functions.inicial()], fg_color="#00adb5", hover_color="#f05454", width=20, height=20)
    back_button.place(relx=1.0, rely=1.0,anchor="se", x=-10, y=-10)

    login_app.mainloop()