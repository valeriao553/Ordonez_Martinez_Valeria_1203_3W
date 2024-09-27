#Examen
#Par o impar
print(" ")
print("Ordonez Martinez Valeria 3W, Ejercicio 8")
print(" ")
#Declaramos las variables con los numero pares e impares
x=[2,4,6,8,10]
y=[1,3,5,7,9]
#Imprimimos mensaje para ingresar un numero
num=input("Ingresa un numero de 1 a 10 para saber si es par o impar: ")
#Convertir el numero ingresado a entero
a=int(num)

#Agregar condicion para que si a esta en la variable x el numero sea par
if a in x:
   #Imprimir que el numero e par
   print("El numero es par")
   #Agregar condicion para que si a esta en la variable y el numero sea impar
elif a in y:
   #Imprimir el numero es impar
   print("Es impar")
   #Si el numero ingresado no se encuentra dentro de 10 se imprima este mensaje
else:
   print("No se encuentra dentro de los primeros 10 numeros")
   