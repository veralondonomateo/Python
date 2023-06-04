print("¡Hola!")
print("Vamos a conocer si el triángulo existe y que tipo de triángulo es")
print("Danos el primer lado del triángulo")
firts_side = int(input())
print("Danos el segundo lado del triángulo")
second_side = int(input())
print("Danos el tercer lado del triángulo")
third_side = int(input())

if firts_side + second_side < third_side or firts_side + third_side < second_side or second_side + third_side < firts_side:
    print("El triángulo no existe")
elif firts_side != second_side != third_side and  firts_side != third_side != second_side :
    print("El triángulo es escaleno")
elif firts_side == second_side == third_side:
    print("El triángulo es equilatero")
elif firts_side == second_side != third_side or third_side == second_side != firts_side or firts_side == third_side != second_side:
    print("El triángulo es isoceles")


