#Operadores 

#Suma
answer = 30 + 12
print("Suma: ",answer)

#Sustracción (Resta)
difference = 30 - 12
print("Resta: ",difference)

#Multiplicación
product = 30 * 12
print("Multiplicacion: ",product)

#División
quotient = 30 / 12
print("Division",quotient)

#División de piso //
seconds = 1042
display_minutes = 1042 // 60
print(display_minutes)

#Jerarquia de Operaciones
result_1 = 1032 + 26 * 2
result_2 = 1032 + (26 * 2)

#Cadenas a Números
demo_int = int('215')
print(demo_int)

demo_float = float('215.3')
print(demo_float)

#Valores Absolutos
print(abs(39 - 16))
print(abs(16 - 39))

#Redondeo
print(round(14.5))

#Biblioteca Math
from math import ceil, floor

round_up = ceil(12.5) #Redondeo hacia arriba más cercano 
print(round_up)

round_down = floor(12.5) #Redondeo hacia abajo
print(round_down)

planet_1 = input('Ingresa la distancia del planeta 1: ')
planet_2 = input('Ingresa la distancia del planeta 2: ')

planet_1 = int (planet_1)
planet_2 = int (planet_2)

distance_km = planet_2 - planet_1
print(abs(distance_km))

distance_mi = distance_km * 0.621
print(distance_mi)