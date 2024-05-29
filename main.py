import customtkinter as ctk
from tkinter import messagebox
from LogIn import login_screen  # importamos la funcion login
from register import add_user_screen
from center import center_window

def main():
    app = ctk.CTk()
    app.title("Log-In")
    center_window(app, 500, 400)
    app.configure(fg_color="#EEEEEE")

    ctk.CTkLabel(app, text="Bienvenido a Tic-Tac-Toe", font=("Helvetica", 30), text_color="#686D76").pack(pady=60)

    login_button = ctk.CTkButton(app, text="Log-In", command=lambda: [app.destroy(), login_screen()], text_color="#373A40", fg_color="#DC5F00", hover_color="#686D76")
    login_button.pack(pady=20)

    login_button = ctk.CTkButton(app, text="Registrar", command=lambda: [app.destroy(), add_user_screen()], text_color="#373A40", fg_color="#DC5F00", hover_color="#686D76")
    login_button.pack(pady=20)

    app.mainloop()

if __name__ == '__main__':
    main()

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("#EEEEEE")
ctk.deactivate_automatic_dpi_awareness()