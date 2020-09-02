#Conditionals Challenge 20: Rock, Paper, Scissors App
import random

print("Bienvenido al juego de Piedra, Papel o Tijeras.\n")

#Se inicializan variables que se utilizaran , lista de las opciones del juego y el user input del numero de rondas que se jugaran
opciones = ["Piedra","Papel","Tijeras"]
cpu_wins = 0
jugador_wins = 0
num_rounds = int(input("¿Cuantos rounds quieres jugar? "))

#Ciclo para repetir las rondas que el usuario decidio
for ronda in range(1,num_rounds+1):
    print("\nRONDA",str(ronda))
    print(f"Jugador: {jugador_wins}\tComputadora:{cpu_wins}")
    eleccion_jug = input("\nTiempo de elegir...piedra, papel O tijeras: ").title().strip()
    eleccion_cpu = random.choice(opciones)

    #Veridica si es una opcion valida, en caso de que si continuea con el proceso, de lo contrario cpu obtiene el punto y no puestra opciones elegidas
    if eleccion_jug in opciones:
        print("\tComputadora:",eleccion_cpu)
        print("\tJugador:",eleccion_jug)
        #Decidir quien gana cuando el usuario decide Piedra y sumarle punto al ganador (cpu o jugador)
        if eleccion_jug == 'Piedra':
            if eleccion_cpu == 'Piedra':
                print("\tEs un empate, que aburrido!\n\tEste round fue un empate.")
            elif eleccion_cpu == 'Papel':
                print("\tPapel envuelve a Piedra!\n\tLa computadora gana el round",ronda)
                cpu_wins +=1
            elif eleccion_cpu == 'Tijeras':
                print("\tPiedra rompe Tijeras!\n\tGanaste el round",ronda)
                jugador_wins +=1
        #Decidir quien gana cuando el usuario decide Papel y sumarle punto al ganador (cpu o jugador)
        elif eleccion_jug == 'Papel':
            if eleccion_cpu == 'Papel':
                print("\tEs un empate, que aburrido!\n\tEste round fue un empate.")
            elif eleccion_cpu == 'Tijeras':
                print("\tTijeras corta papel!\n\tLa computadora gana el round",ronda)
                cpu_wins +=1
            elif eleccion_cpu == 'Piedra':
                print("\tPapel envuelve a Piedra!\n\tGanaste el round",ronda)
                jugador_wins +=1
        #Decidir quien gana cuando el usuario decide Tijeras y sumarle punto al ganador (cpu o jugador)
        elif eleccion_jug == 'Tijeras':
            if eleccion_cpu == 'Tijeras':
                print("\tEs un empate, que aburrido!\n\tEste round fue un empate.")
            elif eleccion_cpu == 'Papel':
                print("\tTijeras corta papel!\n\tGanaste el round",ronda)
                jugador_wins +=1
            elif eleccion_cpu == 'Piedra':
                print("\tPiedra rompe tijeras!\n\tLa computadora gana el round",ronda)
                cpu_wins +=1
    else:
        print("\tOpcion INVALIDA!\n\tLa computadora gana la ronda.")
        cpu_wins+=1
        
#Resumen de resultados finales
print("Resultados finales")
print("\tRounds jugados:",num_rounds)
print("Ganados jugador:",jugador_wins)
print("Ganados Computadora:",cpu_wins)
if jugador_wins == cpu_wins:
    print("Es un EMPATE!")
elif jugador_wins > cpu_wins:
    print("Ganador: JUGADOR!!! :-)")
else:
    print("Ganador: Computadora :-(")

