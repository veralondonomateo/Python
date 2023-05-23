"""import secrets

if __name__ == '__main__':

    names = ['Devin', 'Simon' ,'Julian','Saul', 'Andres', 'Felipe','Manuela', 'Julieta','Tomas','Ricardo','Miguel' ]
    names_election = 7

    fivenames = secrets.SystemRandom().sample(names, names_election)

    for finallynames in fivenames:
        print("Hola " + finallynames)

#two algoritms

print("Escoge un entero")
objetivo = int(input())
respuest = 0
 
while respuest**2 < objetivo:
    respuest += 1

if respuest**2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es {respuest}')
else:
    print(f'{objetivo} no tiene raiz cuadrada exacta')

#three algoritms - aproximaciones

print('Ingrese un numero')
objetivo = int(input())
elipson = 0.01
paso = elipson**2
respuesta = 0.0

while abs(respuesta**2  - objetivo) >= elipson and respuesta <= objetivo:
    respuesta += paso

if abs(respuesta**2 - objetivo) >= elipson:
    print(f'No se encontro la raiz cuadrada de {objetivo}')
else:
    print(f'la raiz de {objetivo} es {respuesta}')

print(True < False)
print(False < True)"""

#Busqueda Binaria
"""objetivo = int(input("Escoge un numero"))
epsilon = 0.01
limiteinferior = 0.0
alto = max(1.0, objetivo)
respuesta = (alto + limiteinferior) / 2

while abs(respuesta**2 - objetivo ) >= epsilon:
    if respuesta ** 2 < objetivo:
        limiteinferior = respuesta
    else:
        alto = respuesta

    respuesta = (alto + limiteinferior) / 2
print(f'la raiz cuadrada de la respuesta de {objetivo} es {respuesta}')"""


#Funciones y abstracción
"""def suma (a, b):
    total = a + b
    return  total

suma(2,3)"""
"""nombre = 'Mateo'
apellido = 'Vera'
def nombre_completo(nombre , apeliido):
    nombrecompleto = nombre + ' ' + apeliido
    return nombrecompleto


print(nombre_completo)"""

"""def raiz(objetivo, respuesta):
    while respuesta**2 < objetivo:
        respuesta += 1
    if respuesta**2 == objetivo:
        print(f'La raíz cuadrada de {objetivo} es {respuesta}')
    else:
        print(f'{objetivo} no tiene raiz cuadrada')
    

raiz(int(input('Ingresa un numero')), 0)"""

"""def funcion1(argumento1, unafuncion):
    def funcion2(argumento2):
        return argumento2 * 2
    
    valor = funcion2(argumento1)
    return unafuncion(valor)
argumento1 = 1

def funcion3(argumento3):
    return argumento3 + 1

funcion1(argumento1, funcion3)"""


"""def hola(x,y):
    valor = x + y
    print(valor)
    return valor
    
hola(4,5)"""

#Cambio de un valor a otro valor como divisas por ejemplo
"""print('Cambio de millas a kilometros y viceversa \n')
print('Cual es tu objetivo')
print('1-Cambiar de millas a kilometros')
print('2-Cambiar de kilometros a millas')
eleccion = int(input())
if eleccion == 1:
    eleccion2 = float(input('Que numero deseas intervenir'))
    final = eleccion2 * 1.61
    print(f'{eleccion2} millas son igual a {final} kilometros')
elif eleccion == 2:
     eleccion2 = float(input('Que numero deseas intervenir'))
     final = eleccion2 / 1.61
     print(f'{eleccion2} kilometros son iguales a {final} millas')
else:
    print('Debes elegir una opción')"""

"""horas = int(input("Hora de inicio (horas): "))
minutos = int(input("Minuto de inicio (minutos): "))
duracion = int(input("Duración del evento (minutos): "))

if (duracion + minutos) < 60:
    minutosandduracion = duracion + minutos
    print(str(horas) + ":" +str(minutosandduracion))
if (duracion + minutos) > 60 and  (duracion + minutos) < 120:
    horas += 1
    minutosandduracion = (duracion + minutos) - 60
    print(str(horas) + ":" +str(minutosandduracion))"""
   
"""def suma(a, b):
    #Suma dos valores a y b

    #param int a culaquier entero
    #param int b culaquier entero
    #return la sumatoria de a y b
    
    total = a + b
    print(total)
    return total
    
suma(4,8)"""

#Recursividad y factoriales

"""def factorial(n):
   
    Calcula el factorial de n
    n = entero > 0
    returns = n!

    if n == 1:
        return 1
    
    return n * factorial(n-1)

n = int(input("escribe un entero: "))

print(factorial(n))"""

"""numeros = [3 , 5 , 7 ,8 ,9]
for n in numeros:
    newnumbs = iter(numeros)
    next(newnumbs)
    print(next)"""

#Tupla []
"""one_tuple = (2,1)
second_tuple = (6,5,4,3)
second_tuple += one_tuple
print(second_tuple)"""



"""def coordenadas():
    return (5,6)


coordenadas = coordenadas()
print(coordenadas) 
x,y = coordenadas
print(x)
print(y)

#Impuestos
ingreso = float(input('Cuanto es su salario: '))

if ingreso <= 85528:
    impuesto = ingreso * 0.18
    impuestototal = round(impuesto - 556.2)
    print(f'Debes pagar {impuestototal} de impuestos')
else:
    totalmenos = ingreso - 85528
    totalfinal = round(14939.2 + totalmenos * 0.32)
    print(f'Debes pagar {totalfinal} de impuestos')

income = float(input('Choice your year salary:'))
if income < 85528:
    newvariable = income * 0.18 - 556.02
newvariable = round(newvariable,0)
print(newvariable)

#Newproject
experince = int(input('What is your salary range:'))
minimumsalary = 1000000
if experince == minimumsalary:
    print("Your salary is the minimum salary")"""


#Rangos : Comienzo a Fin
"""a_range = range(1,10)
for i in a_range:
   print(i)
one_range = range(0,9,2)
other_range = range (0, 10,2)
for value in one_range:
    print(value)
for valuetwo in other_range:
    print(valuetwo)"""
"""for i in range(0,101,2):
    print(i)"""
"""for i in range(1,100,2):
    print(i)"""


#Listas: Secuencia de objetos- Se puede mutar
"""milista = [1,2,3];
milista[1:];
print(milista[1:]);
milista.append(4);
print(milista);
milista[0]='mateo'
print(milista)
milista.pop()
print(milista)

for element in milista:
    print(element)"""

"""a =[1,2,3]
b = a           #Es mucho mejor clonar cada objeto
print(id(a))    #Para tener un id diferente por cada objeto
print(id(b))"""

"""my_list = range(0,101)
double = [i * 2 for i in my_list]
print(double)
pares = [i for i in my_list if i % 2 == 0]
print(pares)
impares = [i for i in my_list if i % 2 == 1]
print(impares)"""


#Diccionario: Acceder a los valores con llaves
"""Mydictionary = {
    'David': 23,
    'Ricardo':45,
    'Carlos':29
}
Mydictionary['Pedro'] = 30
Mydictionary['Julian'] = 90
print(Mydictionary)
print(Mydictionary['Ricardo'])

for i in Mydictionary.keys():
    print(i)

for i in Mydictionary.values():
    print(i)
for llave, valor in Mydictionary.items():
    print(llave,valor)"""


#PRUEBAS Y DEBBUGING : ELIMINAR LOS BUGS DE MI CODIGO: PRUEBAS DE LA CAJA NEGRA
#CAJA NEGRA
"""import unittest
def suma(num1,num2):
    return abs(num1) + num2
class cajanegratests(unittest.TestCase):
    def test_suma_dos_positivos(self):
        num1 = 5
        num2 = 10
        resultado = suma(num1,num2)

        self.assertEqual(resultado,15)
    def test_sumadosnegativos(self):
        num1 = -10
        num2 = -7
        resultado = suma(num1, num2)

        self.assertEqual(resultado,-17) 
if __name__ == '__main__':
    unittest.main()"""

#CAJA DE CRISTAL
"""import unittest
def mayoriadeedad(edad):
    if edad > 18:
        return True
    else:
        return False
class Pruebadecristal(unittest.TestCase):
    def test_mayor(self):
        edad = 20
        resultado = mayoriadeedad(edad)

        self.assertEqual(resultado, True)
    def test_menor(self):
        edad = 15
        resultado = mayoriadeedad(edad)
        self.assertEqual(resultado, False) 
if __name__ == '__main__':
    unittest.main"""

#EXEPCIONES: try except finally, propia excepción: raise
"""def division(lista, divisor):
    try:
            return[i / divisor for i in lista]
    except: ZeroDivisionError as:
            return lista

lista = list(range(10))
divisor = 0
print(division(lista,divisor))"""


#AFIRMACIONES
#Utilizamos assert para manejar las excepciones 
