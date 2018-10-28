
jubilado=str(input("te has jubilado?"))
hombre=str(input("eres un hombre?"))
mujer=str(input("eres una mujer?"))
rubia=str(input("eres rubia?"))
if (jubilado=="si" )or((mujer=="si")and(rubia=="si")):
    print("gratis")
if(hombre=="si")and(jubilado!="si"):
    print:("pagas 1")
if((hombre=="si")and(mujer=="si")and(jubilado!="si")and(rubia!="si")):
    print("pagas 0,5")
