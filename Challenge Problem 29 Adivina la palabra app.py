#Challenge 29: Guess My Word App
import random


print("Bienvenido a la aplicacion de adivinar la palabra\n")

game_categories = {"deportes":["beisbol","futbol","basquetbol","volleybol","soccer"],
                   "colores":["azul","amarillo","verde","morado","blanco"],
                   "frutas":["platano","manzana","guayaba","melon","sandia"] 
                   }

running = True
#ciclo para jugar de nuevo
while running:
    #random items, value, key
    random_category_items = random.choice(list(game_categories.items()))
    random_category = random_category_items[0]#Categoria random
    random_word = random.choice(random_category_items[1]) #Palabra random

    print("Adivina la palabra de " + str(len(random_word)) + " letras de la siguiente categoria:", random_category + "\n")

    #Crear lista vacia del tamaño de la palabra a adivinar 
    hide_word = []
    list_random_w = list(random_word)
    #print(list_random_w)
    #guarda la palabra oculta
    for i in list_random_w:
        hide_word.append("_")    


    lenght_word = len(list_random_w)
    play = True
    intentos = 1
    #Ciclo en el que se adivina la palabra
    while play:
        
        #print(hide_word,"\n")
        #imprime la palabra oculta
        for i in hide_word:
            print(i,end=' ')
        guessing_word = input("\n\nIngresa la palabra que deseas adivinar: ").strip().lower()

        #Si adivina se para el bucle del juego 
        if guessing_word == random_word:
            print(f"Felicidades, adivinaste la palabra en {intentos} intentos.\n")
            play = False
            #Pregunta si quiere volver a jugar ,si decide que no se para el primer bucle y el programa
            running = input("¿Deseas jugar de nuevo?(si/no)").lower().strip() 
            if running.startswith("n"):
                print("Gracias por jugar nuestro juego.")
                running = False
        else:
            print("Es incorrecto. Te revelaremos una letra para ayudarte un poco.")
            swapping = True
            while swapping: #Para que se descubra la palabra 
                letra_random = random.randint(0,lenght_word-1) #Genera un numero (indice) random pero se repite
                if hide_word[letra_random] == "_":
                    hide_word[letra_random] = random_word[letra_random] #Sustituye el indice de la letra random en la palabra oculta
                    swapping = False
                    
            intentos+=1



    
        

    
  




