yB = int(input("Por favor ingrese el año del inicio\n"))
yE = int(input("Por favor ingrese el año del fianl\n"))

for i in range(yB, yE):
    if(not i % 4 and (i % 100 or not i & 400)):
        print(i, " este año es bisiesto")
    elif(i % 10 == 0):
        print(i, " este año es multiplo de 10")
