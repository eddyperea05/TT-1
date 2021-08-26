iteraciones = int(
    input("Por favor ingresar el numero de vez que va a iterar: "))
sum = 0
for i in range(iteraciones):
    num = int(input("Ingrese un numero: "))
    sum += num
print("La sumatoria de lo numeros es " + str(sum))
