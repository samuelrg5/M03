edad = int(input("Indique su edad: "))
sexo=str(input("indique su sexo:"))
if((edad<=5)or(edad >=65)):
    print ("gratis")
else:
    print("tienes que pagar 0,5")
if ((sexo=="hombre")and(edad>5)or(edad<65)):
    print("tienes que pagar 1")
else:
    print ("tienes que pagar 0,5")
