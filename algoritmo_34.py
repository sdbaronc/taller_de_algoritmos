a=int(input("ingrese un numero"))
b=int(input("ingrese un numero"))
c=int(input("ingrese un numero"))
if a>b and a>c:
    print("el nmero mayor es:",a)
if b>a and b>c:
    print("el numero mayor es: ",b)
if c>a and c>b:
    print("el numero mayor es: ",c)
else:
    print("los tres numeros son iguales o los dos numeros mayores son iguales")