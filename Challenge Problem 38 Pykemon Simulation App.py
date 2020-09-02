#Challenge Problem 38 Pykemon Simulation App
import random
#Clases

class Pykemon():
    def __init__(self,name,element,health,speed):
        self.name = name.title()
        self.e_type = element
        self.max_health = health
        self.current_health = health
        self.speed = speed
        self.is_alive = True
    
    def light_attack(self,enemy_pykemon):
        damage = random.randint(15,25)
        
        print("Pykemon " + self.name + " uses: ")
        print("Type of move: light attack")

        print("It deal with " + str(damage) + " damage.")
        enemy_pykemon.current_health -= damage

    def heavy_attack(self,enemy_pykemon):
        damage = random.randint(0,50)
        
        print("Pykemon " + self.name + " uses: ")
        print("Type of move: Heavy attack" )

        if damage < 10:
            print("Attack missed")
        else:
            print("It deal with " + str(damage) + " damage.")
            enemy_pykemon.current_health -= damage


    def restore(self):
        heal = random.randint(15,25)
        self.current_health += heal
        print(self.name + " recovered " + str(heal) + " of health.")
        #Print a message stating that the Pykemon performed a specific attack.
        #Use the Pykemon’s name and the name of the move.
        print("Pykemon " + self.name + " used: restore") 

        if self.current_health > self.max_health:
            self.current_health = self.max_health

    #Clase que determinara cuando el pokemon se desmaye/muera
    def faint(self):
        if self.current_health <= 0:
            self.current_health = 0
            self.is_alive = False
            print(self.name + " has been fainted. ")
            input("Press enter to continue...")
    
    def show_stats(self):
        print("\nName: " + self.name)
        print("Element type: " + self.e_type)
        print("Health: " + str(self.current_health) + "/" + str(self.max_health))
        print("Speed: " + str(self.speed))
    
#Clase hija de Pykemon
class Fire(Pykemon):
    def __init__(self,name,element,health,speed):
        super().__init__(name,element,health,speed)
        #light attack, heavy attack, restore move, and special attack for all water Pykemon.
        self.moves = ["Scratch", "Ember", "Light", "Fire Blast"]
    
    # A attack that can damage a lot according of the pykemon type
    def special_attack(self,enemy_pykemon):
        #Use the Pykemon’s name and the name of the move.
        print(self.name + "uses " + self.moves[3])

        if enemy_pykemon.e_type == "GRASS":
            print("This attack is super effective against grass pykemons")
            damage = random.randint(35,50)
        elif enemy_pykemon.e_type == "WATER":
            print("This attack is not super effective against water pykemons")
            damage = random.randint(5,10)
        else:
            damage = random.randint(10,30)
        
        print("It deal with " + str(damage) + " damage.")
        enemy_pykemon.current_health -= damage
    
    def move_info(self):
        print("\n" + self.name + " Moves: ")
        print("-- Scratch --\nAn efficient attack...\nGuaranteed to do damage within the range of 15 to 25 damage points.")
        print("-- Ember --\nA risky attack...\nCould deal up to 50 damage points or as little as 0 damage points.")
        print("-- Light --\nA restorative move...\nGuaranteed to heal your Pykemon 15 to 25 health points.")
        print("-- Fire Blast --\nA powerful FIRE based attack...\nGuaranteed to deal MASSIVE damage to GRASS type Pykemon.")

class Grass(Pykemon):
    def __init__(self,name,element,health,speed):
        super().__init__(name,element,health,speed)
        #self.name = "Spatol"
        #self.e_type = "GRASS"
        #self.health = 89
        #self.speed = 10
        self.moves = ["Vine Whip", "Wrap", "Grow", "Leaf Blade"]
    
    def move_info(self):
        print("\n" + self.name + " Moves: ")
        print("-- Vine Whip --\nAn efficient attack...\nGuaranteed to do damage within the range of 15 to 25 damage points.")    
        print("-- Wrap --\nA risky attack...\nCould deal up to 50 damage points or as little as 0 damage points.")
        print("-- Grow --\nA restorative move...\nGuaranteed to heal your Pykemon 15 to 25 health points.")
        print("-- Leaf Blade --\nA powerful GRASS based attack...\nGuaranteed to deal MASSIVE damage to WATER type Pykemon.")
    
     # A attack that can damage a lot according of the pykemon type
    def special_attack(self,enemy_pykemon):
        #Use the Pykemon’s name and the name of the move.
        print(self.name + "uses " + self.moves[3])

        if enemy_pykemon.e_type == "WATER":
            print("This attack is super effective against grass pykemons")
            damage = random.randint(35,50)
        elif enemy_pykemon.e_type == "FIRE":
            print("This attack is not super effective against water pykemons")
            damage = random.randint(5,10)
        else:
            damage = random.randint(10,20)
        
        print("It deal with " + str(damage) + " damage.")
        enemy_pykemon.current_health -= damage


class Water(Pykemon):
    def __init__(self,name,element,health,speed):
        super().__init__(name,element,health,speed)
        #self.name = "Pyonx"
        #self.e_type = "WATER"
        #self.health = 80
        #self.speed = 4
        #light attack, heavy attack, restore move, and special attack for all water Pykemon.
        self.moves = ["Bite", "Splash", "Dive", "Water Cannon"]
    
    # A attack that can damage a lot according of the pykemon type
    def special_attack(self,enemy_pykemon):
        #Use the Pykemon’s name and the name of the move.
        print(self.name + "uses " + self.moves[3])

        if enemy_pykemon.e_type == "FIRE":
            print("This attack is super effective against grass pykemons")
            damage = random.randint(35,50)
        elif enemy_pykemon.e_type == "GRASS":
            print("This attack is not super effective against water pykemons")
            damage = random.randint(5,10)
        else:
            damage = random.randint(10,20)
        
        print("It deal with " + str(damage) + " damage.")
        enemy_pykemon.current_health -= damage
    
    def move_info(self):
        print("\n" + self.name + " Moves: ")
        print("-- Bite --\nAn efficient attack...\nGuaranteed to do damage within the range of 15 to 25 damage points.")    
        print("-- Splash --\nA risky attack...\nCould deal up to 50 damage points or as little as 0 damage points.")
        print("-- Dive --\nA restorative move...\nGuaranteed to heal your Pykemon 15 to 25 health points.")
        print("-- Water Cannon --\nA powerful WATER based attack...\nGuaranteed to deal MASSIVE damage to FIRE type Pykemon.")


class Game():
    def __init__(self):
        self.pykemon_elements = ["FIRE","WATER","GRASS"]
        self.pykemon_names = ['Chewdie', 'Spatol','Burnmander', 'Pykachu', 'Pyonx', 'Abbacab', 'Sweetil', 'Jampot',
        'Hownstooth', 'Swagilybo', 'Muttle', 'Zantbat', 'Wiggly Poof', 'Rubblesaur']
        self.battles_won = 0
    
    #Metodo que se encargara de crear un pykemon al azar, retornara un pykemon
    def create_pykemon(self):
        health = random.randint(70,100)
        speed = random.randint(1,10)
        element = random.choice(self.pykemon_elements)
        name = random.choice(self.pykemon_names)

        if element == "FIRE":
            random_pykemon = Fire(name,element,health,speed)
        elif element == "WATER":
            random_pykemon = Water(name,element,health,speed)
        else:
            random_pykemon = Grass(name,element,health,speed)
            
        return random_pykemon

    #Metodo encargado de escoger un pykemon
    def choose_pykemon(self):
        starters = []

        while len(starters) < 3:
            #Crear un pykemon llamando al metodo create_pykemon dentro de la clase actual (game)
            new_pykemon = self.create_pykemon()
            valid_pykemon = True

            for i in starters:
                #Check if the given starter’s name is equal to the currently created Pykemon’s name or if the starter’s element is equal to the
                #currently created Pykemon’s element. We do not want repeated
                #Pykemon names or elements in our starter options.
                if i.name == new_pykemon.name  or i.e_type == new_pykemon.e_type:
                    valid_pykemon = False
                
            if valid_pykemon:
                starters.append(new_pykemon)

        for i in starters:
            #LLamo al metodo show stats para mostrar sus stats
            i.show_stats()
            #Llamo al metodo move_info para mostrar los movimientos que tiene dicho pokemon
            i.move_info()
        
        #Presenta 3 pykemons diferentes para que el usuario eliga uno de ellos
        print("\nDaniel Camberos presents you with three Pykemon:")
        print("(1) - " + starters[0].name)
        print("(2) - " + starters[1].name)
        print("(3) - " + starters[2].name)

        valid_move = True
        while valid_move:
            choice = int(input("Which Pykemon would you like to choose: "))
            if choice < 1 or choice > 3:
                print("\nInvalid choice! try again..")
            else:
                chosen_pykemon = starters[choice-1]
                print("\nCongratulations Trainer! You have choosen " + starters[choice-1].name)
                valid_move = False

        return chosen_pykemon


    #Metodo encargado de seleccionar el ataque que el jugador desea realizar
    def get_attack(self,pykemon):
        print("What move would you like to do? ")
        print("(1) - " + pykemon.moves[0])
        print("(2) - " + pykemon.moves[1])
        print("(3) - " + pykemon.moves[2])
        print("(4) - " + pykemon.moves[3])

        move_choice = int(input("Please enter your move choice: "))
        print("\n------------------------------------------")
        return move_choice
    
    #Llama los metodos del ataque dependiendo del movimiento que desea realizar el jugador
    def player_attack(self,move,player,computer):
        if move == 1:
            player.light_attack(computer)
        elif move == 2:
            player.heavy_attack(computer)
        elif move == 3:
            player.restore()
        elif move == 4:
            player.special_attack(computer)
        
        #Verificar si el pykemon de la computadora ya se murio
        computer.faint()

    #Llama los metodos del ataque dependiendo del movimiento qrealiza la computadora
    def computer_attack(self,player,computer):
        move = random.randint(1,4)
        if move == 1:
            computer.light_attack(player)
        elif move == 2:
            computer.heavy_attack(player)
        elif move == 3:
            computer.restore()
        elif move == 4:
            computer.special_attack(player)
        
        #Verificar si el pykemon del jugador ya se murio
        player.faint()
    
    def battle(self,player,computer):
        #Obtener el movimiento del jugador llamando al metodo get_attack
        move = self.get_attack(player)

        #Si la velocidad del jugador es mayor o igual que la de la pc, jugador ataca primero, de lo contrario pc atacara primero
        if player.speed >= computer.speed:
            self.player_attack(move,player,computer)
            if computer.is_alive == True:
                self.computer_attack(player,computer)
        else:
            self.computer_attack(player,computer)
            if player.is_alive == True:
                self.player_attack(self.get_attack(player),computer,player)

#Main

print("Welcome to Pykemon!")
print("Can you become the worlds greatest Pykemon Trainer???")

print("\nDon't worry! Daniel Camberos is here to help you on your quest.")
print("He would like to gift you your first Pykemon!")
print("Here are three potential Pykemon partners.")

input("\nPress Enter to choose your Pykemon!\n")

playing_main = True
#Se crea el objeto de main
while playing_main:
    game = Game()
    #El jugador debe escoger un pykemon
    player_pykemon = game.choose_pykemon()
    player_pykemon.move_info()
    input("\nYour jorney with " + player_pykemon.name + " begings now...Press Enter")

   #Mientras el pykemon del jugado siga vivo...
    while player_pykemon.is_alive:
        #Se creara un pykemon para la computadora
        computer_pykemon = game.create_pykemon()
        print("\nOH NO! A wild" + computer_pykemon.name + " has approached!")
        computer_pykemon.show_stats()
        print("")
        #Mientras el pykemon del jugador y de la computadora esten vivos...
        while player_pykemon.is_alive and computer_pykemon.is_alive:
            #Se llama al metodo battle y se le pasan los dos objetos (jugador y pc) para simular la pelea
            game.battle(player_pykemon,computer_pykemon)
            #Si ambos pykemons siguen vivos se mostraran las stats que llevan
            if player_pykemon.is_alive and computer_pykemon.is_alive:
                print("-------------------------------Your Stats---------------------------------------")
                player_pykemon.show_stats()
                print("")
                print("---------------------------------Computer stats---------------------------------")
                computer_pykemon.show_stats()
                print("--------------------------------------------------------------------------------")
            #Si solamente esta vivo el jugador quiere decir que la pc murio y se le sumara uno al atributo de las batallas ganadas
        if player_pykemon.is_alive:
            game.battles_won+=1
    #En caso de que el pykemon del jugador ya no este vivo se saldra del loop y mostrara el sig mensaje
    print("")
    print(player_pykemon.name + " has fainted.")
    print("You defeated a total of " + str(game.battles_won) + " Pykemons.")

    #Se le notificara al usuario si quiere volver a jugar, en caso de que no se saldra del loop inicial 
    play_again = input("\nWould you like to play again? (y/n)")
    if play_again.startswith("n"):
        print("Thank you for playing Pykemon! ")
        playing_main = False
