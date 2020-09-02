#Classes Challenge 36: Pythonagachi Simulator App
import random

class Creature():
    def __init__(self,name):
        self.name = name.title()
        self.hunger = 0
        self.boredom = 0
        self.tiredness = 0
        self.dirtiness = 0
        self.food = 2
        self.is_sleeping = False
        self.is_alive = True

    def eat(self):
        if self.food > 0:
            self.food -= 1
            #Decrementa del 1 al 4 la hambre
            dec = random.randint(1,4)
            self.hunger -= dec
            print(self.name + " acaba de comer una deliciosa comida.")
            print(dec)
        else:
            print(self.name + " no tiene comida!")

        #Si la hambre decrementa mas de 4 se le asignara 0  para que no sea negativo
        if self.hunger < 0:
            pass
            self.hunger = 0

    def play(self):
        #Juego de adivinar el numero , si es correcto decrementara mas el aburrimiento, de lo contrario casi no decrementara.
        print(self.name + " quiere jugar un juego.")
        print(self.name + " esta pensando en un numero...los numeros son 0,1 o 2")
        creature_number = random.randint(0,2)
        guess = int(input("Adivina cual numero esta pensando: "))
        if guess == creature_number:
            self.boredom -= 3 
            print("Es correcto!! Adivinaste el numero")
        else:
            self.boredom -= 1
            print("Es incorrecto!! No adivinaste el numero")

        if self.boredom < 0:
            self.boredom = 0

    def sleep(self):
        self.is_sleeping = True
        self.boredom -= 2
        self.tiredness -= 3
        print(self.name + " esta dormiendo.")
        print("Zzzzz...zzzzZ")

        if self.boredom < 0:
            self.boredom = 0
        if self.tiredness <0:
            self.tiredness = 0

    def awake(self):
        sueño = random.randint(0,2)
        print(sueño)
        if sueño == 0:
            print(self.name + " desperto!")
            self.is_sleeping = False
            self.boredom = 0
        else:
            print(self.name + " no desperto...")
            self.sleep()

    def clean(self):
        self.dirtiness = 0
        print(self.name + " ha sido bañado.")

    def forage(self):
        food_increase = random.randint(0,4)
        self.food += food_increase
        self.dirtiness +=2
        print(self.name + " encontró " + str(food_increase) + " piezas de comida!")
    
    def show_values(self):
        print("Hambre (0-10): " + str(self.hunger))
        print("Aburricion (0-10): " + str(self.boredom))
        print("Agotamiento (0-10): " + str(self.tiredness))
        print("Suciedad (0-10): " + str(self.dirtiness))

        print("\nInventario de comida: " + str(self.food))
        if self.is_sleeping:
            print("Estado actual: Dormido")
        else:
             print("Estado actual: Despierto")

    def increment_values(self,nivel):
        self.hunger += random.randint(0,nivel)
        self.dirtiness += random.randint(0,nivel)
        
        if self.is_sleeping == False:
            self.boredom += random.randint(0,nivel)
            self.tiredness += random.randint(0,nivel)
            if self.boredom >= 10:
                self.boredom = 10
            if self.tiredness >= 10:
                self.tiredness = 10
    
    def kill(self):
        if self.hunger >= 10:
            print("Es una pena, " +  self.name + " murió de hambre. " )
            self.is_alive = False
        elif self.boredom >= 10:
            self.boredom = 10
            print(self.name + " esta muy aburrido y se durmio " )
            self.is_sleeping = True
        elif self.tiredness >= 10:
             self.tiredness = 10
             print(self.name + " esta muy cansado y se durmio" )
             self.is_sleeping = True
        elif self.dirtiness >= 10:
             print("Es una pena, " +  self.name + " sufrio una infección y  murió. " )
             self.is_alive = False
    
def show_menu(creatura):
    
    if creatura.is_sleeping == True:
        print("\nEnter (6) para despertarlo.")
        opcion = input("¿Cual es tu opcion? : ")
        opcion = "6"
    else:
        print("\nEnter (1) para alimentarlo.")
        print("Enter (2) para jugar con el.")
        print("Enter (3) para dormirlo.")
        print("Enter (4) para bañarlo.")
        print("Enter (5) para dejarlo buscar comida.")
        opcion = input("¿Cual es tu opcion? : ")
   
    return opcion

def call_action(creatura,opcion):
    if opcion == "1":
        creatura.eat()
    elif opcion == "2":
        creatura.play()
    elif opcion == "3":
        creatura.sleep()
    elif opcion == "4":
        creatura.clean()
    elif opcion == "5":
        creatura.forage()
    elif opcion == "6":
        creatura.awake()
    else:
        print("Opcion no valida")
    
#Main
print("Welcome to the Pythonagachi Simulator App")
playing = True
while playing:
    #Inputs iniciales
    nombre = input("\nQue nombre te gustaria darle a tu mascota Pythonogachi: ").strip().title()
    level = int(input("Favor de ingresar un nivel de dificultad(1-5): "))

    #Creacion del objeto jugador
    player = Creature(nombre)
    rounds = 1
    new_game = True
    while player.is_alive:
        print("-------------------------------------------------")
        print("Round: " + str(rounds))

        print("\nNombre de la creatura: " + nombre)
        player.show_values()

        #Se almacena la opcion elegida
        opcion = show_menu(player)
        
        #Funcion que va a llamar al metodo correspondiente de acuerdo a la opcion elegida
        call_action(player,opcion)

        #Muestra un resumen 
        print("\nResumen de Round " + str(rounds)+"\n")
        player.show_values()
        input("\nPresiona Enter para continuar...")
        
        #Incrementar valores 
        player.increment_values(level)
        player.kill()
        
        rounds+=1

    print("R.I.P.")
    print(player.name + " sobrevivio un total de " + str(rounds-1) + ".")
    repeat = input("¿Te gustaria jugar de nuevo? (s/n): ")
    if repeat.startswith("s"):
        new_game = True 
    else:
        playing = False

print("Gracias por haber jugado Pythonagachi!")
        
    
        
