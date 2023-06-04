print("Adivina un numero entre 1 y 100")
print("Escribe un numero")
numero= int(input())
while numero != 56:
    print("Elige una nueva opcion")
    nuevaeleccion = int(input())
    if (nuevaeleccion == 56):
        break
    elif nuevaeleccion < 56:
        print("Es un numero mayor")
    elif nuevaeleccion > 56:
        print("Es un numero menor")   
print("Adivinaste el numero")