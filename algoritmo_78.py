c=int(input("Digita el numero de bultos: "))

masPes=0
menosPes=0
numBultos=0
pesoTotal=0
valorTotal=0

for i in range(0,c):
	a=int(input("Digita el peso: "))
	if i==0 and a<500:
		masPes=a
		menosPes=a
	if a<menosPes and a!=0:
		menosPes=a
	if a>masPes and a<501:
		masPes=a
	if a!=0 and a>0 and a<=25:
		numBultos+=1
		pesoTotal=pesoTotal+a
	if a!=0 and a>25 and a<=300:
		numBultos+=1
		pesoTotal=pesoTotal+a
		valorTotal=valorTotal+(a*1500)
	if a!=0 and a>300 and a<=500:
		numBultos+=1
		pesoTotal=pesoTotal+a
		valorTotal=valorTotal+(a*2500)
	if a>500:
		print("El bulto excede el peso maximo")
	if a==0:
		break
	if pesoTotal>1800:
		print("No se puede subir al avion el peso es " + str(pesoTotal) + " el peso tiene que ser menor o igual a 1800")

prom=pesoTotal/numBultos
dolar=valorTotal/3165
print("El numero total de bultos fue: " + str(numBultos))
print("El peso mayor fue: " + str(masPes) + " y el menor fue: " + str(menosPes))
print("El peso promedio de los bultos es de: " + str(prom))
print("El precio en dolar fue de: " + str(dolar))
print("El precio en peso colombiano es de: " + str(valorTotal))
print("El peso de todos los bultos fue de: " + str(pesoTotal))