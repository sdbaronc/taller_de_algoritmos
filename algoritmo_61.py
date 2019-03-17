n=int(input("ingrese el primer numero del rango"))
m=int(input("ingrese el segundo numero dell rango"))
if n<m:
    for i in range(n, m):
        print(i)
else:
    print("ingrese otros valores donde el primer numero sea menor que el segundo")
