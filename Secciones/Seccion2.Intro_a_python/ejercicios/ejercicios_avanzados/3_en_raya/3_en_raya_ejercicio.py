# -*- coding: utf-8 -*-
"""

Ejercicio. 3 en Raya

Este ejercicio nos va a ayudar a afianzar los conocimientos adquiridos sobre flujo
de control, y estructuras de datos

Vamos a hacer un programa que nos permita jugar al 3 en raya desde la terminal


Básicamente el panel de 3 en raya son 3 listas dentro de otra

tablero = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
]

por ejemplo, si queremos ver cual es el estado de la casilla de arriba a la
izquerda, podemos acceder haciendo tablero[[0,0]]

Tenemos a 2 jugadores, que turno por turno iran eligiendo coordenadas en el tablero
y poniendo una ficha, una "X" para el jugador 1 y un circulo "O" para el jugador 2


El juego tendrá que validar que las casillas que elijan los jugadores no estén ya
ocupadas por una ficha (es decir, solo se pueden actualizar casillas que sean 0)

"""


from collections import deque

"""
Un deque es una lista donde se pueden insertar elementos por la izquierda y por la
derecha.

Tiene un método llamado rotate que simplemente "rota" los elementos.
Es decir, rotate() pone el ultimo elemento del deque el primero, el primer
elemento el segundo etcétera.
"""

turno = deque(["O", "X"])


tablero = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

# Podemos crear una funcion, cambiar_turno() que rota el deque de turnos y devuelve
# el jugador activo


def cambiar_turno():
    turno.rotate()
    return turno[0]

def mostrar_tablero():
    print("")
    for row in tablero:
        print([square for square in row])

def procesar_posicion(posicion):
    fila,columna = posicion.split(",")
    return int(fila) - 1, int(columna) - 1

def posicion_valida(posicion):
    if 0 <= posicion[0] <=2 and 0 <= posicion[1] <=2:
        if tablero[posicion[0]][posicion[1]] == " ":
            return True
    return False

def actualizar_tablero(posicion, jugador):
    tablero[posicion[0]][posicion[1]] = jugador
    
def evaluar_victoria(j):
    if tablero[0] == [j, j, j] or tablero[1] == [j, j, j]  or tablero[2] == [j, j, j] :
        return True
    elif tablero[0][0] == j and tablero[1][0] == j and tablero[2][0] == j:
        return True
    elif tablero[0][1] == j and tablero[1][1] == j and tablero[2][1] == j:
        return True
    elif tablero[0][2] == j and tablero[1][2] == j and tablero[2][2] == j:
        return True
    elif tablero[0][0] == j and tablero[1][1] == j and tablero[2][2] == j:
        return True
    elif tablero[0][2] == j and tablero[1][1] == j and tablero[2][0] == j:
        return True
    return 

def evaluar_empate():
    return set(tablero[0]).union(set(tablero[1])).union(set(tablero[2])) == set(["X","O"])


def juego():
    jugador = cambiar_turno()
    while True:
        posicion_str = input("Jugador {}, elige una posicion (fila,columna) de 1 a 3. 'salir' para salir: ".format(jugador))
        if posicion_str == "salir":
            print("Adios!")
            break
        try:
            posicion_procesada = procesar_posicion(posicion_str)
        except:
            print("Error, posicion {} no es valida. Formato debe ser (fila,columna)".format(posicion_str))
            continue
        if posicion_valida(posicion_procesada):
            actualizar_tablero(posicion_procesada, jugador)
            mostrar_tablero()
            if evaluar_victoria(jugador):
                print("jugador {} ha ganado!. \nAdios!".format(jugador))
                break
            if evaluar_empate():
                print("Empate!. \nAdios!")
                break
            jugador = cambiar_turno()
        else:
            print("Posicion {} no valida".format(posicion_str))


if __name__ == "__main__":
    juego()