l=int(input("ingres la medida del lado del hexagono"))
import math
ap= math.sqrt((l * l) - ((l * l) / 4))
area= ((l*6)*ap)/2
print("el area del hexagono es: ",area)
