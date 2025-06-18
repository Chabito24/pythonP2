# CONVERSIONES
from time import process_time

# conversiones IMPLICITAS

num1 = 20
print(num1)
print(type(num1))

num2 = 30.5
print(num2)
print(type(num2))


resultado = num1 + num2
print(resultado)
print(type(resultado)) # Este tipo de conversiones las hace automaticamente Python

# conversiones EXPLICITAS

num3 = 5.8
print(num3)
print(type(num3))

num4 = int(num3)
print(num4)
print(type(num4)) # lo que hizo fue eliminar los decimales de num 3 esto no es redondeo es eliminacion de decimales


# ejercicio 2 de conversiones explicitas

edad = (input("Dime tu edad: ")) #capturamo la edad
print(type(edad)) # tipo STR
edad = int(edad) # edad es un tipo de dato String STR pero con esta linea de codigo lo convertimos a INT
print(type(edad)) # cambio a STR
nueva_edad = 1 + edad # creamos una nueva variable tipo INT y sumamos edad la cual ya es un INT con la conversion de la linea anterior
print(nueva_edad) #realizo la suma de edad + 1 ya que ambos datos son el mismo tipo y no genera error

# paso de INT a STR para concatenar (NO usar ver d2p5, aunque esta es una opcion no se recomienda

nueva_edad = str(nueva_edad)
print(type(nueva_edad))
print("en tu proximo cumpleaños tendras" + " " + nueva_edad + " años")
