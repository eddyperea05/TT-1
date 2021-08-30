voto = input("Por favor ingrese su voto\n" +
             "Las posibilidades son:\n" +
             "candidato A por el partido rojo, \n" +
             "candidato B por el partido verde,\n" +
             "candidato C por el partido azul. (A,B,C)\n").upper()

if voto == 'A':
    print("Usted ha votado por el partido Rojo")
elif voto == 'B':
    print("Usted ha votado por el partido Verde")
elif voto == 'C':
    print("Usted ha votado por el partido Azul")
else:
    print("Opción errónea")
