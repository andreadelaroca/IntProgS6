import time
import os

cont = 10
while cont >= 0:
    with open('andrea.txt', 'w', encoding = 'utf-8') as archivo:
        archivo.write(f"Numero {cont}")
    if cont >= 6 and cont <= 10:
        os.system("color A2")
    elif cont > 3 and cont < 6:
        os.system("color E6")
    elif cont <= 3:
        os.system("color C4")
    print(cont)
    time.sleep(1)
    cont -= 1
    
os.system("cls || clear")
os.system("color a3")
print("Bienvenido a la Carrera de ISI")
os.system("pause")