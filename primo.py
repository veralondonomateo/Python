print("Ingrese el numero del que quiere saber si es primo o compuesto")
numero= int(input(""))
x=0
c=0
while x < numero:
    x+=1
    if numero%x==0:
        print(x)
        c+=1
    else:
        pass

if c>2:
    print ("El número ingresado es compuesto, y sus divisores son los anteriores")
else:
    print ("El número es primo, ya que solo se puede dividir por el 1 y por si mismo")