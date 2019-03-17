n=int(input("ifrese un numero"))
if n<0 and n%2==0:
    print("el numero es par negativo")
if n<0 and n%2!=0:
    print("el numero es impar negativo")
if n>0 and n%2==0:
    print("el numero es par positivo")
if n>0 and n%2!=0:
    print("el numero es impar positivo")
else:
    print("indefinido")
