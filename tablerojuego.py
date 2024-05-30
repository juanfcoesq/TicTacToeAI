import customtkinter as ctk
from tkinter import messagebox
from movimientos_compu import movimiento_ia, movimiento_ia_tontito
from center import center_window
import random
import menu
import time
from conect import connect_to_db

global modojuego, nummovs, turno, nombrejugador1, nombrejugador2, tablero, listaBotones, puntos


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


def inicio(juego):
    global modojuego, nummovs, turno, nombrejugador1, nombrejugador2, tablero, listaBotones, ventana, puntos
    # 0 1v1 , 1 dificil, 2 facil y 3 nivel medio
    a = ""
    match juego:
        case 0:
            a = "1v1"
            puntos = 0
        case 1:
            a = "DIFICIL"
            puntos = 500
        case 3:
            a = "INTERMEDIO"
            puntos = 100
        case 2:
            a = "FACIL"
            puntos = 20
        case 4:
            a = "SIMULACION DE JUEGO"
            puntos = 0

    ventana = ctk.CTk()
    ventana.geometry('545x720')
    ventana.title("MODO DE JUEGO: " + a)
    ventana.configure(bg='#222831')
    center_window(ventana, 545, 720)
    modojuego = juego
    nummovs = 0
    turno = 0
    nombrejugador1 = "X"
    nombrejugador2 = "O"
    listaBotones = []
    tablero = ["N"] * 9

    # Crear botones del tablero
    for i in range(0, 9):
        boton = ctk.CTkButton(
            ventana,
            text='',
            width=125,
            height=125,
            corner_radius=10,
            font=("Helvetica", 24),
            command=lambda num=i: movimiento(num),
            fg_color="#1f1f1f",
            text_color="#ffffff"
        )
        listaBotones.append(boton)
        boton.grid(row=i // 3, column=i % 3, padx=27.5, pady=27.5)

    # Etiqueta para mostrar el turno del jugador

    # Botón para iniciar el juego
    iniciar = ctk.CTkButton(
        ventana,
        text='Iniciar Juego',
        width=200,
        height=50,
        corner_radius=10,
        font=("Helvetica", 16),
        command=comienzo,
        fg_color="#393e46",
        text_color="#00adb5"
    )
    iniciar.grid(row=4, column=0, columnspan=3, pady=20)

    bloquear()
    ventana.mainloop()


def bloquear():
    global listaBotones
    for i in range(0, 9):
        listaBotones[i].configure(state="disabled")


def comienzo():
    global nombrejugador1, nombrejugador2, listaBotones, tablero
    for i in range(0, 9):
        listaBotones[i].configure(state="normal", fg_color="#1f1f1f", text="")
        tablero[i] = "N"

    numero_aleatorio = random.randint(1, 2)
    if (numero_aleatorio == 1 and not (modojuego == 0)) or modojuego==4:
        ia_move = movimiento_ia_tontito(tablero, "O")
        movimiento_ia_jugada(ia_move, "O")
        if modojuego==4:
            time.sleep(1)
            ventana.update()

    while not (verificar()) and modojuego==4:
        ia_move = movimiento_ia(tablero, "X")
        movimiento_ia_jugada(ia_move, "X")
        time.sleep(1)
        ventana.update()
        ia_move = movimiento_ia(tablero, "O")
        movimiento_ia_jugada(ia_move, "O")
        time.sleep(1)
        ventana.update()


def movimiento(num):
    global turno, nombrejugador1, nombrejugador2, tablero, listaBotones, nummovs, modojuego
    if tablero[num] == "N" and turno == 0:
        listaBotones[num].configure(text="X", fg_color="#00adb5", text_color="#000000", font=("Helvetica", 40, "bold"))
        tablero[num] = "X"
        listaBotones[num].configure(state="disabled")
        if not verificar():
            turno = 1
            if modojuego == 1 or (modojuego == 3 and nummovs % 2 == 0):
                ia_move = movimiento_ia(tablero, "O")
                movimiento_ia_jugada(ia_move, "O")
            if modojuego == 2 or (modojuego == 3 and nummovs % 2 == 1):
                ia_move = movimiento_ia_tontito(tablero, "O")
                movimiento_ia_jugada(ia_move, "O")

            nummovs = nummovs + 1

    if tablero[num] == "N" and turno == 1:
        listaBotones[num].configure(text="0", fg_color="#f05454", text_color="#000000", font=("Helvetica", 40, "bold"))
        tablero[num] = "0"
        listaBotones[num].configure(state="disabled")
        if not verificar():
            turno = 0


def movimiento_ia_jugada(num, caract):
    global turno, nombrejugador1, nombrejugador2, tablero, listaBotones
    color = "#f05454"
    if caract == "X":
        color = "#00adb5"

    if tablero[num] == "N":
        listaBotones[num].configure(text=caract, fg_color=color, text_color="#000000", font=("Helvetica", 40, "bold"))
        tablero[num] = caract
        listaBotones[num].configure(state="disabled")
        if not verificar():
            turno = 0


def verificar():
    bandera = False
    global turno

    condiciones_ganadoras = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for (a, b, c) in condiciones_ganadoras:
        if tablero[a] == tablero[b] == tablero[c] != "N":
            ganador = nombrejugador1 if tablero[a] == "X" else nombrejugador2
            sumarscore(ganador)
            ventana.destroy()
            menu.menu()
            bandera = True
            break

    if bandera:
        turno = 0
        bloquear()
    elif all(spot != "N" for spot in tablero):
        bloquear()
        messagebox.showinfo("SE TERMINO", "EMPATE, NADIE GANA")
        ventana.destroy()
        menu.menu()
        bandera = True

    return bandera


def sumarscore(ganador):
    global modojuego, puntos
    user_id = id
    if not (modojuego == 0) and (ganador == "X") and not (modojuego == 4):

        #SACAMOS EL SCORE QUE TIENE
        conn = connect_to_db()
        cursor = conn.cursor()

        # Ejecutar la consulta
        query = f"SELECT score FROM accounts WHERE id = '{user_id}';"
        cursor.execute(query)
        results = cursor.fetchone()  # fetchone() es más apropiado si esperas un solo resultado

        if results:
            # Asegurarse de que el resultado sea un entero
            current_score = int(results[0])

            # Sumar puntos al resultado actual
            new_score = current_score + puntos

            # Actualizar el nuevo score en la base de datos
            update_query = f"UPDATE accounts SET score = %s WHERE id = %s;"
            cursor.execute(update_query, (new_score, user_id))
            conn.commit()

        cursor.close()
        conn.close()

        messagebox.showinfo("SE TERMINO", f"GANASTE! PUNTUACION GANADA: {puntos}")
    elif modojuego == 0 or modojuego == 4:

        messagebox.showinfo("SE TERMINO", f"GANASTE JUGADOR: {ganador}")

    else:
        messagebox.showinfo("SE TERMINO", "PERDISTE  CONTRA LA MAQUINA :(")
