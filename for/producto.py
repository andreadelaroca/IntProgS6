import os
os.system("color 07")
producto = input("Producto: ")
precio = int(input("Precio: "))
cantidad = int(input("Cantidad: "))
if cantidad < 0:
    print(f"\033[31m{cantidad}\033[0m")
else:
    print(f"\033[31m{cantidad}\033[0m")

with open("productos.txt", "a", encoding = "utf-8") as p:
    p.write(f"\nProducto: {producto}\nPrecio: {precio}\nCantidad: {cantidad}\nTotal: {precio*cantidad}\n")
    p.write("="*10)
    p.write("\n")
    
print("\nArchivo guardado")