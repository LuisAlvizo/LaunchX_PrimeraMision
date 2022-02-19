# program.py
from traceback import print_tb
from datetime import date

sum = 1 + 2
print(sum)

# Funcion print
print('Hola desde la Consola')

# Variables
sum = 1 + 2 
product = sum * 2
print(product)

# Tipos de Datos
# Declaramos la Variable
distancia_a_alfa_centauri = 4.367

# Descubrimos su tipo de Dato
print(type(distancia_a_alfa_centauri))

# Operadores Aritmeticos
left_side = 10
right_side = 5
print(left_side / right_side) #2

# Operadores de Asignación
x = 3
x += 10
print(x) #13

# Fechas
# Obtenemos la fecha de hoy
date.today()

# Mostramos la fecha en la consola
print(date.today())

# Conversion de tipo de datos
print("Today's date is: " + str(date.today()))

# Entrada del Usuario
print("Bienvenido al programa de bienvenida")
name = input("Introduzca su nombre ")
print("Saludos: " + name)

print("Calculadora")
first_number = input("Primer número: ")
second_number = input("Segundo número: ")
print(int(first_number) + int(second_number))