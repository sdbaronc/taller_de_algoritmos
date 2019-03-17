dec=0

bin=input("Digita el numero binario que deceas convertir: ")

for num in bin:
	dec=dec*2+int(num)

print("El numero " + str(bin) + " en decimal es " + str(dec))