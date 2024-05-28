import subprocess
from center import center_window
from game import start_game
import customtkinter as ctk
from tkinter import messagebox
from scoreboard import score_screen
from config import config_screen

def menu():
    menu_app = ctk.CTk()
    menu_app.title("Tic Tac Toe")
    center_window(menu_app, 600, 500)

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

    game = ctk.CTkButton(menu_app, text="Iniciar Juego", command=on_select_mode)
    game.pack(pady=20)

    button_frame = ctk.CTkFrame(menu_app, fg_color="transparent")
    button_frame.pack(pady=40)

    score_button = ctk.CTkButton(button_frame, text="Scoreboard", command=lambda: [score_screen()] )
    score_button.pack(side=ctk.LEFT, pady=10, padx=10)

    config_button = ctk.CTkButton(button_frame, text="Configuración", command=lambda: [config_screen()])
    config_button.pack(side=ctk.LEFT, pady=10, padx=10)

    back_button = ctk.CTkButton(menu_app, text="Regresar",command=lambda: [menu_app.destroy(), subprocess.Popen(["python", "main.py"])])
    back_button.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

    menu_app.mainloop()