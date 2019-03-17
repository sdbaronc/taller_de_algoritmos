d=int(input("Digita la distancia de tu destino,"))
n_dias=int(input("Digita la cantidad de dias"))
valor_d=d*5000
valor_descuento=valor_d*0.15
valor_viajed=int(valor_d-valor_descuento)
if d<=20:
	print("El valor de tu pasaje es de 100000")
elif d>=1000 and n_dias>=7:
	print("El valor de tu pasaje es de ",valor_viajed)
else:
	print("El valor de tu pasaje es de ",valor_d)