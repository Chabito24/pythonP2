"""
Vendedores reciben un total de 13% por sus ventas totales, se deben
calcular las comisiones teniendo en cuenta los siguientes datos

1. Nombre
2. ventas

respuesta debe generar una frase que incluya el nombre y el monto
en comision que le corresponde por sus ventas

la respuesta no debetener mas de 2 decimales
"""

nombre = input("nombre completo: ") # variable para almacenar el nombre
ventas = input("ventas totales: ") # variable para almacenar las ventas
mes = input("mes a calcular: ") # cree una variable adicionar para almacenar el mes donde se pagan las comisiones
ventas = float(ventas) # se pasa STR a INT
comisiones = round(ventas*0.13,2) # variable con redondeo


print(f"OK, para {nombre} las comisiones generadas en el mes de {mes} son de ${comisiones}")

