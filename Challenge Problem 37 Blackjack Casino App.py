#Classes Challenge 36: Pythonagachi Simulator App
import random
import time

class Card():
    """Clase que define lo que vale la carta, rank, el tipo"""
    def __init__(self,rank,value,suit):
        self.rank = rank
        self.value = value
        self.suit = suit

    def display_card(self):
        print(self.rank + " of " + self.suit)

class Deck():
     """Clase que simulara la creacion de la baraja"""

     def __init__(self):
        self.cards = []

     def build_deck(self):
        #clubs (♣), diamonds (♦), hearts (♥) and spades (♠)
        suits = ["clubs","diamons","hearts","spades"]
        value_card = {"A":11,
                      "2":2,
                      "3":3,
                      "4":4,
                      "5":5,
                      "6":6,
                      "7":7,
                      "8":8,
                      "9":9,
                      "10":10,
                      "J":10,
                      "Q":10,
                      "K":10, }
        for s in suits:
            for k,v in value_card.items():
                card = [s,k,v]
                self.cards.append(card)

     def shuffle_deck(self):
        #Se barajera (random.shuffle ordenara de forma aleatorias las cartas)
        random.shuffle(self.cards)

     def deal_card(self):
        """Metodo para elegir una carta de la baraja"""
        choosen_card = self.cards.pop()
        return choosen_card
    
class Player():
    """Clase que se usara para controlar el juego del jugador"""

    def __init__(self):
        self.player_hand = []
        self.hand_value = 0
        self.playing_hand = True

    def draw_hand(self,deck_cards):
        """Metodo para repartir dos cartas al jugador""" #Deck_cards es el objeto de deck para poder llamar a uno de sus metodos
        for i in range(2):
            carta_repartida = deck_cards.deal_card()
            self.player_hand.append(carta_repartida)

    def display_hand(self):
        #Mostrar las cartas que se tiene
        print("\nPlayer's hand")
        for card in self.player_hand:
            card = Card(card[1],card[2],card[0])
            card.display_card()
            
    def hit(self,deck_cards):
        #Si se desea tomar otra carta
        extra_card = deck_cards.deal_card()
        self.player_hand.append(extra_card)

    def get_hand_value(self):
        #Obtener la suma de las cartas del jugador
        self.hand_value = 0
        as_in_hand = False

        for card in self.player_hand:
            self.hand_value += card[2]
            if card[1] == "A":
                as_in_hand = True
        if self.hand_value > 21 and as_in_hand == True:
            self.hand_value -= 10
        print("Total value of hand is " + str(self.hand_value))    

    def update_hand(self,deck_cards):
        """Actualizara las cartas del usuario dependiendo si quiere tomar otra carta o no y tornara False su turno"""
        if self.hand_value < 21:
            decision = input("\nWould you like to take another card? (yes/no) ")
            if decision == "yes":
                self.hit(deck_cards)
               
            else:
                self.playing_hand = False
                
        else:
             self.playing_hand = False
        
class Dealer():
    """Clase que se usara para controlar el juego de la PC"""
    
    def __init__(self):
        self.dealer_hand = []
        self.hand_value = 0
        self.playing_hand = True

    def draw_hand(self,deck_cards):
        """Metodo para repartir dos cartas al jugador""" #Deck_cards es el objeto de deck para poder llamar a uno de sus metodos
        for i in range(2):
            carta_repartida = deck_cards.deal_card()
            self.dealer_hand.append(carta_repartida)

    def display_hand(self):
        input("Press enter to reveal the dealer cards")
        print("Dealer's hand")
        for card in self.dealer_hand:
            ####Reveal an individual card by calling the cards display_card() method.###
            card = Card(card[1],card[2],card[0])
            card.display_card()
            time.sleep(1)

    def hit(self,deck_cards):
        self.get_hand_value()
        while self.hand_value < 17:
            gotten_card = deck_cards.deal_card()
            self.dealer_hand.append(gotten_card)
            self.get_hand_value()
        total_cards = len(self.dealer_hand)
        print("\nDealer is set with a total of " + str(total_cards) + " cards.")
        

    def get_hand_value(self):
        #Obtener la suma de las cartas del dealer
        self.hand_value = 0
        as_in_hand = False

        for card in self.dealer_hand:
            self.hand_value += card[2]
            if card[1] == "A":
                as_in_hand = True
        if self.hand_value > 21 and as_in_hand == True:
            self.hand_value -= 10
        #print("Total value of hand is " + self.hand_value)    
    

class Game():
    def __init__(self,money):
        self.money = money
        self.bet = 20
        self.winner = " "

    def set_bet(self):
        betting = True
        while betting:
            money_bet = int(input("\nHow much money are you willing to play with today(20 minimum): "))
            if money_bet < 20:
                self.bet = 20
            elif money_bet > self.money:
                print("You don't have enought money")
                
            else:
                self.bet = money_bet
                betting = False
                
    def scoring(self,player_hand,dealer_hand):
        if player_hand == 21:
            print("Player got blackjack! You won!\n")
            self.winner = "p"
        elif dealer_hand == 21:
            print("Dealer gots blackjack! Dealer Won!\n")
            self.winner = "d"
        elif player_hand > 21:
            print("Player went over 21. You Loose!\n")
            self.winner = "d"
        elif dealer_hand > 21:
            print("Dealer went over 21. Dealer Loose\n")
            self.winner = "p"
        elif player_hand > 21 and dealer_hand > 21:
            print("It was a tie! Both have more than\n")
            self.winner = "tie"
        else:
            if player_hand > dealer_hand:
                print("Dealer won because he has highest value\n")
                self.winner = "d"
            elif dealer_hand > player_hand:
                print("Player won because he has highest value\n")
                self.winner = "p"
            else:
                print("It was a tie!\n")
                self.winner = "tie"

    def payout(self):
        if self.winner == "p":
            self.money = self.money + self.bet
            
        elif self.winner == "d":
            self.money = self.money - self.bet

    def display_money(self):
        print("Current money: " + str(self.money))

    def display_money_and_bet(self):
        print("Current money: " + str(self.money) + "\tCurrent bet: " + str(self.bet))
    
    
#Main
print("Welcome to the BlackJack Casino")
print("The minimum bet at this table is $20.")
my_money = int(input("\nHow much money are you willing to play with today: "))

#Game object
current_game = Game(my_money)

playing = True
while playing:
    
    #Inputs iniciales
    game_deck = Deck()
    #Crear la baraja del juego
    game_deck.build_deck()
    #Barajear/revolver la baraja
    game_deck.shuffle_deck()

    #Player and dealer objects
    dealer = Dealer()
    player = Player()

    #   Mostrar el dinero actual de la apuesta y del jugador. Colocar la apuesta
    current_game.display_money()
    current_game.set_bet()

    #Repartir cartas al jugador y al dealer
    player.draw_hand(game_deck)
    dealer.draw_hand(game_deck)

    #Muesta el dinero actual y la apuesta
    current_game.display_money_and_bet()

    #The dealer is showing a K of Clubs.
    dealer_card = dealer.dealer_hand[0]
    #print("The dealer is showing a K of Clubs.")
    print("\nThe dealer is showing a " + dealer_card[1]  + " of " + dealer_card[0])

    while player.playing_hand:
        #Muestra el juego del jugador, el valor y lo actualiza (en caso de tener A)
        player.display_hand()
        player.get_hand_value()
        player.update_hand(game_deck)

    #Para que la pc tome una carta hasta llegar a 17 y mostrar sus cartas
    dealer.hit(game_deck)
    dealer.display_hand()

    #Calcular el score de la ronda y determinar si ganaste o perdiste para pagar la apuesta.
    """Se agrega como parametro el atributo de hand_value para que lo compare en el metodo de scorering"""
    current_game.scoring(player.hand_value,dealer.hand_value)
    current_game.payout()

    if my_money < 20:
        playing = False
        print("The user doesn't have enough money to do a bet, because doesn't have the minimum.")
    else:
        keep_playing = input("\nWould you like to keep playing? (Yes/No)")
        if keep_playing.startswith("N"):
            print("Thank you for playing blackjack casino! Bye.")
            playing = False

            
            
    
        
