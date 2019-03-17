seg=int(input("Digita la cantidad de segundos: "))
min=seg/60
seg_2=int(seg%60)
horas=int(min/60)
min_2=int(min%60)
print("Tiempo ",horas,":",min_2, ":",seg_2)