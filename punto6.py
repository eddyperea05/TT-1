num = int(input("Por favor ingrese un numero entero positivo: "))
while True:
    if(num > 0):
        break
    num = int(input(
        "Por favor ingrese un numero entero positivo, el anterior fue negativo o 0: "))
for i in range(num, (num*2)):
    print(i)
