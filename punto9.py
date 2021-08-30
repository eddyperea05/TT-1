num1 = int(input("Por favor ingrese un primer numero\n"))
num2 = int(input("Por favor ingrese un segundo numero\n"))
sum = 0
for i in range(num1, num2+1):
    sum += i
print("La suma de los numeros en el ", num1, " y ", num2, " Es ", sum)