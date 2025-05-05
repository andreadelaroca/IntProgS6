#tabla de multiplicar de un número

while True:
    num = int(input("Ingrese un número entero positivo: "))
    if num > 0:
        break
    print("Intente otra vez")

for i in range(1,11):
    resultado = num * i
    print(f"{num} x {i} = {resultado}")
