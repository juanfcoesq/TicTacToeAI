import subprocess
from customtkinter import CTkImage
from center import center_window
from game import start_game
import customtkinter as ctk
from tkinter import messagebox
from scoreboard import score_screen
from config import config_screen
from tablerojuego import inicio
import main_functions

def menu():
    menu_app = ctk.CTk()
    menu_app.title("Tic Tac Toe")
    center_window(menu_app, 700, 600)

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

    mode_var = ctk.StringVar(value="0")

    label = ctk.CTkLabel(menu_app, text="Seleccione el modo de juego:", text_color="#686D76", font=("Helvetica", 40))
    label.pack(pady=20)

    frame = ctk.CTkFrame(menu_app, fg_color="transparent")
    frame.pack(pady=20, anchor="center")

    modes = [
        ("Jugador vs Jugador", "0"),
        ("Jugador vs Máquina (Fácil)", "2"),
        ("Jugador vs Máquina (Intermedio)", "3"),
        ("Jugador vs IA (Difícil)", "1")
    ]

    for i, (text, value) in enumerate(modes):
        radio = ctk.CTkRadioButton(frame, text=text, variable=mode_var, value=value, fg_color="#00adb5", hover_color="#f05454")
        radio.pack(anchor="w", pady=10)

    game = ctk.CTkButton(menu_app, text="Iniciar Juego", command=lambda: [menu_app.destroy(), inicio(int(mode_var.get()))], fg_color="#00adb5", hover_color="#f05454")
    game.pack(pady=20)

    button_frame = ctk.CTkFrame(menu_app, fg_color="transparent")
    button_frame.pack(pady=40)

    score_button = ctk.CTkButton(button_frame, text="Scoreboard", command=lambda: [score_screen()], fg_color="#00adb5", hover_color="#f05454")
    score_button.pack(side=ctk.LEFT, pady=10, padx=10)

    config_button = ctk.CTkButton(button_frame, text="Configuración", command=lambda: [menu_app.destroy(), config_screen()], fg_color="#00adb5", hover_color="#f05454")
    config_button.pack(side=ctk.LEFT, pady=10, padx=10)

    back_button = ctk.CTkButton(menu_app, text="Regresar",command=lambda: [menu_app.destroy(), main_functions.inicial()], fg_color="#00adb5", hover_color="#f05454", width=20, height=20)
    back_button.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

    menu_app.mainloop()