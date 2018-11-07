Anyo_actual= int(input("En que año estamos?"))
Anyo_futuro= int(input("Que año sera?"))
if((Anyo_actual==0)or(Anyo_futuro==0)):
        print("Error")
else:
    if (Anyo_futuro==Anyo_actual):
        print("Son el mismo año")
    else:
   
        Diferencia_1=(Anyo_futuro-Anyo_actual)
        Diferencia_2=(Anyo_actual-Anyo_futuro)
        if(Anyo_futuro>Anyo_actual):
            print("Faltan" ,Diferencia_1, "años para" ,Anyo_futuro,)
        else:
            if(Anyo_futuro<Anyo_actual):
                print("Han pasado",Diferencia_2,"años desde",Anyo_futuro,)
        
        
