#Functions Challenge 33: Bank Deposit and Withdrawal App

def get_info():
    user_info = {"name":" ",
                "savings":0,
                "cheking":0}
    user_info["name"] = input("Hello, what is your name: ").strip().lower().title()
    user_info["savings"] = float(input("How much money would you like to set up your savings account with: "))
    user_info["cheking"] = float(input("How much money would you like to set up your checking account with: "))

    return user_info

def display_info(user_info):
    print("\nCurrent Account Information: ")
    for k,v in user_info.items():
        if k == "name":
            print(str(k.title()) + ": " + str(v))
        else:
            print(str(k.title()) + ": $" + str(v))
        
def repeticion():
    validar = True
    while validar:
        decision = input("\nWould you like to make another transaction (y/n):").lower()
        if decision.startswith("n"):
            print("Thank you. Have a great day!")
            return False
            validar = False
        elif decision.startswith("y"):
            return True
            validar = False
        else:
            print("Invalid (Available options y = yes , n = no)")

def make_deposit(user_info, account, money):
        user_info[account]+= money
        print("Depsiting $" + str(money) + " into " + user_info["name"] + "'s savings account.") 
    

def make_withdrawal(user_info, account, money):
    if user_info[account] - money >= 0:
        user_info[account]-= money    
        print("Withdrew $" + str(money) + " from " +user_info["name"]+ "'s savings account.")

    else:    
        print(f"Sorry, by withdrawing ${money} you will have a negative balance.")
        
    

#main
print("Welcome to the Python First National Bank.\n")

#Variable que contendra el diccionario con la info
info = get_info()

ejecutando = True
while ejecutando:
    
    #Display info con el diccionario de parametro
    display_info(info)

    #Inputs del tipo de cuenta, tipo transaccion y dinero
    type_acc = input("\nWhat account would you like to access (Savings or Checking): ").strip().lower()
    type_trans = input("What type of transaction would you like to make (Deposit or Withdrawal): ").lower().strip()
    money = float(input("How much money: "))

    #Si la cuenta es savings o cheking y si se desea depositar o retirar, se llamara la funcion que le corresponde de lo contrario no se hara nada
    if type_acc == 'savings' or type_acc == 'checking':
        if type_trans == 'deposit':
            make_deposit(info,type_acc,money)
        elif type_trans == 'withdrawal':
            make_withdrawal(info,type_acc,money)
        else:
            print('Im sorry, we cannot do that for you today.')
    else:
        print('Im sorry, we cannot do that for you today.')        

    #Decide si se seguira ejecutando el porgrama o no
    ejecutando = repeticion()


