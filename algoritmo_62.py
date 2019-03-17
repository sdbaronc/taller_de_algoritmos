n=int(input("ingrese el primer numero del rango"))
m=int(input("ingrese el segundo numero dell rango"))
if n<m:
    cont=0
    for i in range(n, m):
        cont=i+cont
    print(cont)
else:
    print("ingrese otros valores donde el primer numero sea menor que el segundo")