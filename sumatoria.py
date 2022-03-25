#sumatoria
suma = 0
cnum = 0
numero = 1
while numero !=0:
    numero = float (input ("numero: "))
    suma = suma + numero
    cnum = cnum+1
    print  ("sumatoria va: ", suma)
    if numero % 2 ==0:
        cpar =cpar+1
    else:
            cim=cim+1
    print ("sumatoria es: ", suma, "cantidad de numeros",cnum-1,"promedio", (suma/cnum+1))
    print ("cantidad pares", cpar)
    