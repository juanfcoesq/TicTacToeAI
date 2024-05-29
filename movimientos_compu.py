import math
import random


def minimax(tablero, jugador, max_jugador):
    ganador = verificar_ganador(tablero)
    if ganador:
        if ganador == max_jugador:
            return {'posicion': None, 'puntuacion': 1}
        elif ganador == 'Empate':
            return {'posicion': None, 'puntuacion': 0}
        else:
            return {'posicion': None, 'puntuacion': -1}

    mejores_movimientos = []
    for i in range(len(tablero)):
        if tablero[i] == "N":
            nuevo_tablero = tablero[:]
            nuevo_tablero[i] = jugador
            puntuacion = minimax(nuevo_tablero, 'O' if jugador == 'X' else 'X', max_jugador)
            puntuacion['posicion'] = i
            mejores_movimientos.append(puntuacion)

    if not mejores_movimientos:
        return {'posicion': None, 'puntuacion': 0}

    if jugador == max_jugador:
        mejor_movimiento = max(mejores_movimientos, key=lambda x: x['puntuacion'])
    else:
        mejor_movimiento = min(mejores_movimientos, key=lambda x: x['puntuacion'])

    return mejor_movimiento

def verificar_ganador(tablero):
    condiciones_ganadoras = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for (a, b, c) in condiciones_ganadoras:
        if tablero[a] == tablero[b] == tablero[c] != "N":
            return tablero[a]

    if "N" not in tablero:
        return 'Empate'

    return None

def movimiento_ia(tablero, jugador):
    max_jugador = jugador
    mejor_movimiento = minimax(tablero, jugador, max_jugador)
    return mejor_movimiento['posicion']

def movimiento_ia_tontito(tablero, jugador):
    posiciones_N = [i for i, letra in enumerate(tablero) if letra == 'N']
    if posiciones_N:
        posicion_aleatoria = random.choice(posiciones_N)
        return posicion_aleatoria
    else:
        return None  #
