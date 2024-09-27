#Examen
#Numeros divisibles por 7 que sean mayores a 70
print(" ")
print("Ordonez Martinez Valeria 3W, Ejercicio 9")
print(" ")
#Declarar variable del numero que introducimos
num=input("Ingrese un numero entero en el rango de 1 a 70: ")
#Convertir a entero
a=int(num)
print(" ")
#Asignar valores a las variables a, b y c
b=[42, 49, 56, 63, 70]
c=[7, 14, 21, 28, 35]
d=[41,43,44,45,46,47,48,50,51,52,53,54,55,57,58,59,60,61,62,64,65,66,67,68,69]
#Agregar ondicion si a esta en b
if a in b:
    print("Si es un numero divisible por 7 y si es mayor a 40")
    print (" ")
    #Agregar condicion si a esta en c
elif a in c:
    print("Si es divisible entre 7 pero no es mayor que 40 ")
    print(" ")
    #Agregar condicion de a esta en d
elif a in d:
    print("El numero si es mayor que 40 pero no es divisible entre 7")
    print (" ")
    #Si no se encuentra en el ranfo sugerido se envia este mensaje
else:
    print("No esta dentro del rango")
    print(" ")