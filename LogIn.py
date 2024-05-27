import customtkinter as ctk
from tkinter import messagebox
from conect import connect_to_db
from center import  center_window
def handle_login(username, password):
    print(f"Nombre de usuario ingresado: {username}")  # Mensaje de depuración
    print(f"Contraseña ingresada: {password}")  # Mensaje de depuración

    if login(username, password):
        messagebox.showinfo("Login Exitoso", "¡Login exitoso!")
    else:
        messagebox.showerror("Error de Login", "Nombre de usuario o contraseña incorrectos.")

def login(username, password):
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
    center_window(login_app, 500, 400)


    ctk.CTkLabel(login_app, text="Log-In", font=("Helvetica", 30)).pack(pady=20)

    label_username = ctk.CTkLabel(login_app, text="Nombre de usuario:", font=("Helvetica", 20))
    label_username.pack(pady=10)

    entry_username = ctk.CTkEntry(login_app)
    entry_username.pack(pady=5)

    label_password = ctk.CTkLabel(login_app, text="Contraseña:", font=("Helvetica", 20))
    label_password.pack(pady=10)

    entry_password = ctk.CTkEntry(login_app, show="*")
    entry_password.pack(pady=5)

    login_button = ctk.CTkButton(login_app, text="Login", command=lambda: handle_login(entry_username.get(), entry_password.get()))
    login_button.pack(pady=20)

    login_app.mainloop()
