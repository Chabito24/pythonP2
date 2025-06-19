# EJERCICIOS FORMATEO DE CADENAS

x = 10
y = 5

print("Mis numeros favoritos son {} y {}" .format(x,y))
print(f"Mis numeros favoritos son {x} y {y}")

# Operaciones

print("la suma de {} y {} es igual a {}" .format(x,y,x+y))
print(f"la suma de {x} y {y} es igual a {x+y}")


# Ejercicio 1 :

"""
 imprimir el nombre y número de asociado dentro de la siguiente frase:

Estimado/a (nombre_asociado), su número de asociado es: (numero_asociado)
"""

nombre_asociado = "Jesse Pinkman"
numero_asociado = 399058
print(f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}")

# Ejercicio 2

"""
Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:

Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos
"""

puntos_nuevos = 350
puntos_totales = 1225

print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")


# Ejercicio 3

"""
Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:

Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos

En esta ocasión, la cantidad de puntos acumulados (totales) será igual a los puntos_anteriores más los puntos_nuevos.
"""

puntos_anteriores = 875
puntos_nuevos = 350

print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_anteriores + puntos_nuevos} puntos")