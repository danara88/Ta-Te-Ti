# -*- coding: utf-8 -*-

"""
Indicaciones: 

Para este proyecto, deberás programar el juego TA-TE-TI. Cuando el programa comienza a correr, en la pantalla 
aparece el tablero de TA-TE-TI (de 3x3) y un input que permite al usuario elegir el símbolo “X” o el símbolo “O”. 
Las “X” empiezan.

El usuario debe elegir la posición del tablero (esta posición debe ser correcta y no debe estar ocupada) donde poner 
el símbolo en el tablero y el sistema valida si el juego termina con un ganador o en empate. Si no hay ganador o la
partida no terminó todavía en empate, el juego continúa preguntando al otro usuario que seleccione la posición del 
tablero dónde quiere poner su símbolo y así siguiendo hasta que la partida termine con un ganador o en empate.
"""

# FUNCIONES DEL PROGRAMA

# Decorador para imprimir la bievenida
def initial_mode(initial = False) :
    def _wrap(func) :
        def inner() :
            if initial == True :
                print("""
    =========================
            Ta-Te-Ti
    =========================
                """)
            return func()
        return inner
    return _wrap


@initial_mode(True)
def print_instructions():
    "Imprime la bienvenida del juego y las instrucciones"

    print("""
    Instrucciones:
    Estas son las posiciones :
        |1| |2| |3|
        |4| |5| |6|
        |7| |8| |9|

    ¡ Ha jugar !

    """)



def print_table() :
    "Imprime la tabla del juego"

    for raw in table_game :
        for i, col in enumerate(raw) :
            if raw[i] == 'X':
                print("    |X|", end="")
            elif raw[i] == 'O' :
                print("    |O|", end="")
            else :
                print("    |_|", end="")
        else :
            print("\n")



def get_table_values() :
    "Retorna todos los valores de la tabla del juego en forma de lista"

    table_values = []
    for raw in table_game :
        for i, col in enumerate(raw) :
            table_values.append(raw[i])
    return table_values



def search_value_table( num, letter ):
    "Función para identificar en que posición de la tabla se puso el símbolo"

    success = False
    for raw in table_game :
        if success :
            break
        for i, col in enumerate(raw):
            if raw[i]  == num and raw[i] != 'X' and raw[i] != 'O':
                raw[i] = letter 
                success = True
                break

    # Llamar a la función para verificar si hay un ganador o no
    winner = verify_winner(letter, get_table_values())
    result = ()
    # Ganan las X
    if winner[0] :
        result = (True, True, False)
       
    # Ganan las O
    elif winner[1] :
        result = (True, False, True)
    
    # Todavía no gana ninguno
    else:                 #  X      O 
        result = (success, False, False)

    return result



def verify_winner(letter, table_values) :
    "Verifica quien ganó la partida"

    win_x = False
    win_o = False

    # Ganar en vertical
    for i in range(10) :
        if i == 3 :
            break
        if table_values[i] == letter and table_values[i+3] == letter and table_values[i+6] == letter :
            if letter == 'X' :
                win_x = True
                break
            if letter == 'O'  :
                win_o = True
                break
    
    # Ejecutar lo siguiente si aún no hay un ganador
    if win_o == False and win_x == False :
        # Ganar en horizontal
        for i in range(10) :
            if i == 0 or i == 3 or i == 6 :
                if table_values[i] == letter and table_values[i+1] == letter and table_values[i+2] == letter :
                    if letter == 'X' :
                        win_x = True
                        break
                    if letter == 'O'  :
                        win_o = True
                        break

    # Ejecutar lo siguiente si aún no hay un ganador
    if win_o == False and win_x == False :
        # Ganar en cruz
        if (table_values[0] == letter and table_values[4] == letter and table_values[8] == letter) or (table_values[2] == letter and table_values[4] == letter and table_values[6] == letter):
            if letter == 'X' :
                win_x = True
            if letter == 'O'  :
                win_o = True
    
    return (win_x, win_o)
    

def is_full_table( table_values ) :
    "Función para verificar si la tabla esta llena o no"
    is_full = False
    symbols = []
    # Recorrer los valores del la tabla
    for item in table_values :
        if item == 'X' or item == 'O':
            # Almacenar en una nueva lista los items con simbolo
            symbols.append(item)
    # Comparar la longitud de ambas listas
    if len(table_values) == len(symbols) :
        is_full = True
    return is_full
  

# Creación de la matriz 3x3
table_game = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Imprimir la bienvenida y las instrucciones del juego
print_instructions()
# Imprimir la tabla inicialmente
print_table()

# Establecer el comienzo de turno 
turn_x = True
turn_o = False

# Comenzar el ciclo para ir preguntando los turnos
while True :
        # Verificar que la tabla no este llena
        full_table = is_full_table( get_table_values() )
        if full_table :
            print('\n    ¡ ES UN EMPATE ! \n')
            break

        try :
            if turn_x :
                # Preguntar al turno de las X donde quiere poner su símbolo
                target_x = int(input("    Turno de las X >> "))
                # Llamar a la función para posicionar el simbolo
                validChange = search_value_table( target_x, "X")
               

            if turn_o :
                # Preguntar al turno de las X donde quiere poner su símbolo
                target_o = int(input("    Turno de las O >> "))
                # Llamar a la función para posicionar el simbolo
                validChange = search_value_table( target_o, "O")


            # Verificar que se haya puesto con éxito el símbolo
            if validChange[0] :
                # Verificar quien ganó
                if validChange[1] :
                    print('\n    ¡ HAN GANADO LAS X !\n')
                    break
                if validChange[2] :
                    print('\n    ¡ HAN GANADO LAS O ! \n')
                    break
                print("    Se ha posicionado tu símbolo correctamente \n")
                
                # Realizar el cambio de turno
                if turn_x :
                    turn_o = True
                    turn_x = False
                elif turn_o :
                    turn_o = False
                    turn_x = True

                # Imprime la tabla
                print_table()

            else:
                # Mostrar mensaje de error si la acción de posicionar un simbolo no ha sido exitoso
                print("    Algo salió mal. No se pudo posicionar tu simbolo. Vuelve a intentarlo .. \n")
                
        except ValueError:
            print('    Opción inválida .. \n')

        
# Imprimir finalmente la tabla
print_table()