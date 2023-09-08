#bibliotecas 

import os 
from time  import sleep

#Inicio

os.system('cls')
print("Painel de Login")
for i in range (1,4): 
    user=input("User:")
    pas=input("Password:")
    os.system("cls")
    
    if user == "admim" and pas == "1234":
        print("Bem-Vindo ",user)
        sleep(2)
        break
    
    else:
        print("Usuario ou senha incorretos!")
        if i == 1: 
            print("Voce tem mais 2 chances!!")
            sleep(0.5)
            os.system('cls')
        if i == 2: 
            print("Voce tem mais 1 chances!!")
            sleep(0.5)
            os.system('cls')    
        if i == 3: 
            print("Voce esgotou seu limite de tentativas!!!!")
            sleep(1)
            os.system('cls')
            break
