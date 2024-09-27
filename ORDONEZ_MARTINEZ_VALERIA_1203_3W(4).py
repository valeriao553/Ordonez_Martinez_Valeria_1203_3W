#Numeros mayores y menores
print(" ")
print ("Ordonez Martinez Valeria 3W, Examen primer parcial")

#Declarar los valores introducidos
valor1=input("Ingrese el primer valor: ")
#Convertir a entero
a=int(valor1)
valor2=input("Ingrese el segundo valor: ")
#Convertir a entero
b=int(valor2)
valor3=input("Ingrese el tercer valor: ")
#Convertir a entero
c=int(valor3)

#Agregar una condicion para que los valores sean distintos
if a == b or a == c or b == c:
    print("Los valores deben ser distintos.")
else:
    # Encontrar el mayor y el menor
    if a > b and a > c:
        may = a
    elif b > a and b > c:
        may = c
    else:
        may = c

    if a < b and a < c:
        men = a
    elif b < a and b < c:
        men = b
    else:
        men = c

    # Imprimir los resultados
    print("El mayor valor es:", may)
    print("El menor valor es:", men)