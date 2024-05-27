import customtkinter as ctk
from tkinter import messagebox
from LogIn import login_screen  # importamos la funcion login
from game import start_game
from register import add_user_screen
from center import center_window

def tictactoe():
    menu_app = ctk.CTk()
    menu_app.title("Tic Tac Toe")
    center_window(menu_app, 500, 400)

    def on_select_mode():
        mode = mode_var.get()
        winner = start_game(mode)
        if winner:
            if winner == 'X':
                msg = "¡El jugador X gana!"
            elif winner == 'O':
                msg = "¡El jugador O gana!"
            else:
                msg = "¡Es un empate!"
            result = messagebox.askyesno("Fin del Juego", f"{msg}\n¿Quieres jugar de nuevo?")
            if not result:
                menu_app.quit()

    mode_var = ctk.StringVar(value="1")

    label = ctk.CTkLabel(menu_app, text="Seleccione el modo de juego:")
    label.pack(pady=20)

    modes = [
        ("Jugador vs Jugador", "1"),
        ("Jugador vs Máquina (Fácil)", "2"),
        ("Jugador vs Máquina (Intermedio)", "3"),
        ("Jugador vs IA (Difícil)", "4")
    ]

    for text, value in modes:
        radio = ctk.CTkRadioButton(menu_app, text=text, variable=mode_var, value=value)
        radio.pack(pady=10)

    button = ctk.CTkButton(menu_app, text="Iniciar Juego", command=on_select_mode)
    button.pack(pady=20)

    menu_app.mainloop()


def main():
    app = ctk.CTk()
    app.title("Log-In")
    center_window(app, 500, 400)

    ctk.CTkLabel(app, text="Bienvenido a Tic-Tac-Toe", font=("Helvetica", 30)).pack(pady=20)

    login_button = ctk.CTkButton(app, text="Log-In", command=lambda: [app.destroy(), login_screen()])
    login_button.pack(pady=20)

    login_button = ctk.CTkButton(app, text="Registrar", command=lambda: [app.destroy(), add_user_screen()])
    login_button.pack(pady=20)

    app.mainloop()


if __name__ == '__main__':
    main()
ctk.set_appearance_mode("system")
ctk.deactivate_automatic_dpi_awareness()