# REDONDEO

resultado = (90/7)
redondeo = round(resultado)

print(resultado)
print(redondeo)

# Ejemplos

#1

valor = 90.666666666666666
valor2 = round(90.666666666666666)

print(round(valor))
print(round(valor,2)) # aqui defino la cantidad de decimales a mostrar en pantala
print(type(valor))
print(type(valor2)) # como se redondeo antes lo pasa a INT

#2

x = 50

print(round(x ** 0.5,2))