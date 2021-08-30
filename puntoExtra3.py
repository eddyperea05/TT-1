num = int(input("Ingrese un numero: "))
tPares = 0
tImpares = 0
while num != 0:
    numPares = 0
    numImpares = 0
    while num != 0:
        ultimodigito = num % 10
        if ultimodigito % 2 == 0:
            numPares += 1
            tPares += 1
        else:
            numImpares += 1
            tImpares += 1
        num = num//10
    print("El número ingresado tiene " + str(numPares),
          " digitos pares y " + str(numImpares), " digitos impares")
    num = int(input("Ingrese otro número: "))
print("Total de dígitos pares: " + str(tPares))
print("Total de dígitos impares: " + str(tImpares))
