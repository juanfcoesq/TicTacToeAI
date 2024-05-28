from center import center_window
from game import start_game
import customtkinter as ctk
from tkinter import messagebox

def menu():
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