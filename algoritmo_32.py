n1=float(input("ingrese la primera nota"))
n2=float(input("ingrese la segunds nota"))
n3=float(input("ingrese la tercera nota"))
n4=float(input("ingrese la cuarta nota"))
n5=float(input("ingrese la quinta nota"))
prom= (n1*0.15)+(n2*0.2)+(n3*0.15)+(n4*0.3)+(n5*0.2)
if prom>=3:
    print("aprobó")
if prom>4.5:
    print("felicitaciones")
if prom<3:
    print("reprobó")
if prom<2:
    print("no puede habilitar")