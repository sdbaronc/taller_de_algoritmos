pos=0
par=0
a=int(input("Digita un numero de inicio: "))

for num in range(a,100+1):
	if num>0:
		pos+=1

	if num>0 and num<=80 and num%2==0:
		par+=1

print("Hay " + str(pos) + " numeros positivos")
print("Hay " + str(par) + " numeros pares")