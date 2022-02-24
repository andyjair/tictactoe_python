from itertools import cycle
import numpy as np

def recibir_input(tablero, jugador):
    turno = ""
    turno = input(f'cual espacio quieres {jugador}?: ')
    turno = [letra for letra in turno]
    try:
        x = int(turno[0]) 
        y = int(turno[1])
        if tablero[x][y] != 'x' and tablero[x][y] != 'o':
            tablero[x][y] = jugador
        else:
            print("tienes que eligir espacio vacio")
            recibir_input(tablero,jugador)
        return tablero
    except:
        print("tienen que ser numeros")
        recibir_input(tablero, jugador)
    
def mostrar_tablero(tablero):
    for x in tablero:
        print(f"{x[0]}|{x[1]}|{x[2]}")
        print("-" * 6)

def verificar_juego(tablero, jugador):
    for fila in tablero:      
        if len(set(fila)) == 1:
            print(f"{jugador} gano")

            return "n"
    for columna in np.transpose(tablero):
        if len(set(columna)) == 1:
            print(f"{jugador} gano")
            return "n"
    if (len(set(tablero[i][i] for i in range(len(tablero))))) == 1:
        print(f"{jugador} gano")
        return "n"
    if ( len( set(tablero[i][len(tablero)-i-1] for i in range(len(tablero))))) == 1:
        print(f"{jugador} gano")
        return "n"

def setup():
    player1 = 'x'
    player2 = 'o'
    tablero = [
        ["00","01","02"], 
        ["10","11","12"], 
        ["20","21","22"]
        ]
    numero_turnos = 0
    return player1, player2, tablero, numero_turnos

def game():
    empezar = input("quieres empezar el juego?[y/n]: ")    
    jugador1, jugador2, tablero, numero_turnos = setup()
    jugadores = cycle([jugador1, jugador2])
    
    while empezar != "n":        
        jugador = next(jugadores)
        tablero = recibir_input(tablero, jugador)
        empezar = verificar_juego(tablero, jugador)
        mostrar_tablero(tablero)
        numero_turnos += 1
        if numero_turnos == 9 and empezar != "n":
            print("empate")
            empezar = "n"
    
    jugar  = input("quieres jugar otra vez?[y/n]: ")
    if jugar == "y":
        game()
        
if __name__ == "__main__":
    game()
    