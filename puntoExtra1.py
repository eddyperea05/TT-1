pos = 0
neg = 0
contP = 0

for i in range (6):
    num = int(input("Ingrese un numero (" + str(i+1) +"/6)\n"))
    if(num >= 0):
        pos += num
        contP += 1
    elif(num < 0):
        neg += num
print("La sumatoria de los numero negativos es: ", neg)
if(contP != 0):
    pos = pos/contP
    print("El promedio de los numeros positivos es: ", int(pos))
else:
    print("No hay ningun numero positivo, por esta razon no se puede promediar")
