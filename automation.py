import time 
import pyautogui
import os

from position import *

def numbers_text():
   print("""
Digite o número que você deseja fazer a automação. 
    
    [1] - Google 
    [2] - Youtube 
    [3] - GitHub 
    [4] - ChatGPT
    [5] - Visual Studio Code
    [6] - Sair do programa
    """)

run = True
while(run):
    numbers_text()
    try: 
        number = int(input("Número: "))
        if number == 1: 
            google()
            os.system('cls')

        elif number == 2: 
            youtube()
            os.system('cls')

        elif number == 3:
            github()
            os.system('cls')

        elif number == 4:
            chatgpt()
            os.system('cls')

        elif number == 5:
            vscode()
            os.system('cls')

        elif number == 6:
            print("Encerrando o programa...")
            time.sleep(1)
            run = False

        else:
            print("Número sem funcionalidade.")
            time.sleep(1)
            os.system('cls')

    except ValueError:
        time.sleep(1)
        print("Só é permitido números. Tente novamente.")
        time.sleep(2)
        os.system('cls')
