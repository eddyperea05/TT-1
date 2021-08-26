iteraciones = int(
    input("Por favor ingresar el numero de vez que va a iterar: "))
negativos = 0
for i in range(iteraciones):
    num = int(input("Ingrese un numero: "))
    if num < 0:
        negativos += 1
print("La cantidad de negativos es " + str(negativos))