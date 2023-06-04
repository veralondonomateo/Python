print("¡Hola!")
print("ingresa un numero entero")
num_1 = int(input())
print("ingrese otro numero entero") 
num_2= int(input())
print("Que operacion deseas realizar con ambos numeros")
print("1.Suma")
print("2.Resta")
print("3.Multiplicación")
print("4.division")
desicion = int(input())
if desicion == 1:
    print("el resultado es " + str(num_1 + num_2))
elif desicion == 2:
    print("el resultado es " + str(num_1 - num_2))
elif desicion == 3:
    print("el resultado es " + str(num_1 * num_2))
elif desicion == 4:
    print("el resultado es " + str(num_1 / num_2) )