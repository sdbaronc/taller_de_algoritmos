a=int(input("ingrese un numero de 4 cifras"))#1234

b=int(a/1000)#1
c=a-(b*1000)#234
d=int(c/100)#2
e=d*10#20
f=c-(d*100)#34
g=int(f/10)#3
h=g*100#300
i=f-(g*10)#4
j=i*1000
invertidos=(b+e+h+j)
print(invertidos)