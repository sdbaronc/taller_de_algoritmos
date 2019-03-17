c=int(input("bultos que va a ingresar: "))#esto lo hago por que ya lo probe con 15 y me parecia buena idea que usted lo intentara con varios bultos
cont1=0
cont2=0
bultos=0
pesoTotal=0
valorTotal=0
for i in range(0,c):
    a=float(input("ingresar peso"))
    if i==0 and a<500:
       cont1=a
       cont2=a
    if a < cont2 and a!=0 :
            cont2 = a
    if a>cont1 and a<501:
            cont1=a
    if a!=0 and a>0 and a<=25:
            bultos+=1
            pesoTotal=pesoTotal+a
    if a!=0 and a>25 and a<=300:
            bultos+=1
            pesoTotal=pesoTotal+a
            valorTotal=valorTotal+(a*1500)
    if a!=0 and a>300 and a<=500:
        bultos+=1
        pesoTotal=pesoTotal+a
        valorTotal=valorTotal+(a*2500)
    if a>500 :
        print("Este bulto no sera puesto en el avion por exceso de peso")
    if a==0 :
        break
if pesoTotal>1800:
     print("no podemos subir esto al avion por que su peso es: ",pesoTotal,"El peso debese menor o igual a 1800")
else:
 if pesoTotal <=1800:
    print("el numero total de bultos es:", bultos)
    print("El peso del bulto mas pesado es", cont1, "\nEl bulto menos pesado es: ", cont2)
    print("El peso promedio de peso cada bulto es", (pesoTotal / bultos))
    print("El precio de el total de bultos en pesos colobiamnos es: ", valorTotal)
    print("el valor por peso en dolares sera: ", (valorTotal * 3165))  # El dvalor del dolar el dia sabado
    print("el  valor por peso de los bultos en colombianos 5es: ",pesoTotal)