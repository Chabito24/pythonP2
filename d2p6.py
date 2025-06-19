# Operadores Matemáticos

x = 6
y = 2
z = 8
zz = 7

print(f"{x} mas {y} es igual a {x + y}")
print(f"{x} menos {y} es igual a {x - y}")
print(f"{x} por {y} es igual a {x * y}")
print(f"{x} dividido {y} es igual a {x / y}") # las divisiones "/" devuelven un valor de tipo float
print(f"{z} dividido al piso de {y} es igual a {x // y}") # la division al piso es con "//" y me devuelve un valor INT
print(f"{zz} dividido al piso de {y} es gual a {x // y}") # aqui lo mismo sabemos que el resultado logico es 3.5 pero al estar al piso me lo regresa sin decimal como un INT

print(f"la variable 'zz' es de tipo {type(zz)}")

# MODULO (esto es lo que conocemos como RESIDUO

"""
En una división matemática, las partes principales son cuatro:

Dividendo:
Es el número que se va a dividir.
Ejemplo: en 12÷3, el dividendo es 12.

Divisor:
Es el número entre el cual se divide el dividendo.
Ejemplo: en 12÷3, el divisor es 3.

Cociente:
Es el resultado de la división (cuántas veces cabe el divisor en el dividendo).
Ejemplo: en 12÷3 = 4, el cociente es 4.

Residuo o resto (solo si no es una división exacta):
Es lo que sobra después de realizar la división, si el dividendo no es divisible exactamente por el divisor.
Ejemplo: 
12÷3=4 y sobra 0 → el residuo es 0.
"""

print(f"{zz} modulo 'residuo' de {y} es igual {zz % y}") # el signo porcentaje intermedio me genera el modulo de la division a correr el código debe generar un 1

# POTENCIA

print(f"{x} elevado a la {y} es igual a {x**y}") # el doble ** me eleva al cuadrado asignando primero la base y posteriormente el exponente
print(f"{x} elevado a la {3} es igual a {x**3}")

# RAIZ CUADRADA

print(f"la raiz cuadrada de {9} es igual a {9**0.5}")
print(f"la raiz cuadrada de {x} es igual a {x**0.5}")
print(f"la respuesta de la raiz de {6} es de tipo {type(x**0.5)}")


