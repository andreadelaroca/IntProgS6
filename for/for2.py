#la tabla de multiplicar de un numero x
import os
def obtener_tabla(num):
    for i in range(13):
        print(f"{i} * {num} = {i * num}")

def main():
    os.system("cls || clear")
    number = int(input("Dime un # "))
    obtener_tabla(number)

main()
