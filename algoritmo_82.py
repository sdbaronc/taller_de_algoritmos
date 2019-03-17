a=int(input("Digita un numero de filas: "))

for i in range(a):
	n="@ "
	for j in range(a):
		if j>=i:
			n+=""
		else:
			n+="@ "
	print(n)