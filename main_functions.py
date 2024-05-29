import customtkinter as ctk
from tkinter import messagebox
from LogIn import login_screen  # importamos la funcion login
from register import add_user_screen
from center import center_window

def inicial():
    app = ctk.CTk()
    app.title("Log-In")
    center_window(app, 700, 600)

    ctk.CTkLabel(app, text="Bienvenido a Tic-Tac-Toe", font=("Helvetica", 50)).pack(pady=90)

    login_button = ctk.CTkButton(app, text="Log-In", command=lambda: [app.destroy(), login_screen()], fg_color="#00adb5", hover_color="#f05454", font=("Helvetica", 30), width=300, height=50)
    login_button.pack(pady=20)

    login_button = ctk.CTkButton(app, text="Registrar", command=lambda: [app.destroy(), add_user_screen()], fg_color="#00adb5", hover_color="#f05454", font=("Helvetica", 30), width=300, height=50)
    login_button.pack(pady=20)

    app.mainloop()

ctk.set_appearance_mode("system")
ctk.deactivate_automatic_dpi_awareness()