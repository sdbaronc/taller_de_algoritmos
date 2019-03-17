n=int(input("Digita el numero de filas: "))

for i in range(n):
	a=" "
	for j in range(n):
		if j>=i:
			a+="* "
		else:
			a+=" "
	print(a)