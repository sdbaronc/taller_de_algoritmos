n=int(input("ingrese el valor de la cuenta"))
sub=n+(n*0.19)
des= sub-(sub*0.05)
if sub>150000:
    print("el valor a pagar es:",des)
else:
    print("el valor a pagar es: ",sub)