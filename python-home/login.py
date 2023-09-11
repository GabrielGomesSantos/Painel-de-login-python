#bibliotecas 

import os 
from time  import sleep
from getpass import getpass
import stdiomask
import json
#Inicio

#Painel de Login e Cadastro
i = True
def menu():
    print("Sistema de Login")
    print("Escolha uma opcao")
    print("[1] Cadastras um novo Usuario (Nao feito)")
    print("[2] Fazer login")
    print("[3] Sair (nao feito)")
    chosen = int(input('Digite sua opcao: '))
    while chosen > 3 or chosen < 1: 
        os.system('cls')
        print("opcao nao encontrado!!")
        print("[1] Cadastras um novo Usuario (Nao feito)")
        print("[2] Fazer login")
        print("[3] Sair (nao feito)")
        chosen = int(input('Digite sua opcao: '))
    return(chosen)
    
    
def fazer_login():
    user = input("User: ")
    pasw = stdiomask.getpass(prompt="Password: ",mask="*")
    return(user, pasw)

def fazer_cadastro():
    user = input("User: ")
    pasw = stdiomask.getpass(prompt="Password: ")
    cadastro={"Usuario:",user,"Senha:",pasw}
    with open("cadastro.json", 'w') as file: 
        json.dump(cadastro, file, indent=4)

    return(user, pasw)

for i in range (1):
    os.system('cls')
    chosen = menu()
    
    if chosen == 1: 

        user = input("User: ")
        pasw = stdiomask.getpass(prompt="Password: ")
        cadastro={
            "Usuario:",user,
            "Senha:",pasw
            }
        with open("cadastro.json", 'w') as file: 
            json.dump(cadastro, file, indent=4)
        
    elif chosen == 2:
        #login 
        print("Login")
        
    elif chosen == 3:
        print("saindo")
        break