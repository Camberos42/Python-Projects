#Functions Challenge 34:Head to Head Tic-Tac-Toe App


def display_tic_tac_toe():
    print("Tic Tac Toc")
    print("~~~~~~~~~~~")
    print("||1||2||3||")
    print("~~~~~~~~~~~")
    print("||4||5||6||")
    print("~~~~~~~~~~~")
    print("||7||8||9||")
    print("~~~~~~~~~~~")
def display_game(game):
    print("\nTic Tac Toc")
    print("~~~~~~~~~~~")
    print("||"+game[0]+"||"+game[1]+"||"+game[2]+"||")
    print("~~~~~~~~~~~")
    print("||"+game[3]+"||"+game[4]+"||"+game[5]+"||")
    print("~~~~~~~~~~~")
    print("||"+game[6]+"||"+game[7]+"||"+game[8]+"||")
    print("~~~~~~~~~~~")

def player_option(game,turno):
    validar = True
    #Valida opcion del player 1 (x)
    while validar:
        t = int(input(f"{turno}: Where would you like to place your piece (1 - 9): "))
        if t <= len(game) and t >= 0:
            if game[t-1] == "_":
                game[t-1] = turno
                validar = False
            else:
                print("That spot has already been chosen. Try again.")
        else:
            print("That is not a spot on the board. Try again.")

def winner(game,turno):
    if (game[0] == turno and game[1] == turno and game[2] == turno) or (game[3] == turno and game[4] == turno and game[5] == turno) or (game[6] == turno and game[7] == turno and game[8] == turno) or (game[0] == turno and game[4] == turno and game[8] == turno) or (game[2] == turno and game[4] == turno and game[6] == turno) or (game[0] == turno and game[3] == turno and game[6] == turno) or (game[1] == turno and game[4] == turno and game[7] == turno) or (game[2] == turno and game[5] == turno and game[8] == turno):
        if turno == "X":
            print("Congratulations! Player1 wins!")
        elif turno == "Y":
            print("Congratulations! Player2 wins!")
        return True
    else:
        return False
   
        
#main

playing = True
posiciones = ["_","_","_","_","_","_","_","_","_"]
game_plays = posiciones.copy()
jugadas = 0

#Muestra las posiciones del juego
display_tic_tac_toe()
#Muestra el juego
display_game(posiciones)

for j in range(1,10):

    #Si es impar sera turno de la x , si es impar sera turno de la o
    if j%2 == 0:
        turno = "Y"
    else:
        turno = "X"

    #Llama la funcion de la opcion del jugador 1 o 2
    player_option(posiciones,turno)

    display_tic_tac_toe()
    display_game(posiciones)
    
    #Valida si hay un ganador y si lo hay detiene el juego, si es empate tambien se acaba
    stop_game = winner(posiciones,turno)
    if stop_game == True:
        break
    if j == 9 and stop_game == False:
        print("\nEs un empate!")

#Para ganar hay 3 formas diferentes
#mismo nivel pos[0-2]"""
#Misma pos de cada nivel n1[0],n2[0],n3[0]"""
#Diferente posicion, Dif nivel pero en orden n1[0],n2[1],n3[2]
