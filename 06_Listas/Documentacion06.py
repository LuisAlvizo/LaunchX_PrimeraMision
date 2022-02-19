#Crear una lista
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

#Acceder a elementos de una lista
print('The first planet is', planets[0])
print('The second planet is', planets[1])
print('The third planet is', planets[2])

#Modificar valores
planets[3] = 'Red Planet'
print('Mars is also known as', planets[3])

#Determinar la longitud de una lista "len" 
number_of_planets = len(planets)
print('There are', number_of_planets, 'planets in the solar system.')

#Agregar valores a listas ".append(value)"
planets.append('Pluto')
number_of_planets = len(planets)
print('There are actually', number_of_planets, 'planets in the solar system.')

#Eliminar valores de una lista ".pop("
planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print('No, there are definitely', number_of_planets, 'planets in the solar system.')

#Indices negativos: -1 devuelve el último elemento de una lista. Un índice de -2 retorna del penúltimo al último.
print('The last planet is', planets[-1])
print('The penultimate planet is', planets[-2])

#Buscar un valor index()
jupiter_index = planets.index('Jupiter')
print('Jupiter is the', jupiter_index + 1, 'planet from the sun')

#Almacenar números en listas
gravity_on_earth = 1.0
gravity_on_the_moon = 0.166

gravity_on_planets = [0.378, 0.907, 1, 0.379, 2.36, 0.916, 0.889, 1.12]

bus_weight = 12650 # in kilograms, on Earth
print('On Earth, a double-decker bus weighs', bus_weight, 'kg')
print('On Mercury, a double-decker bus weighs', bus_weight * gravity_on_planets[0], 'kg')

#min() y max() con listas
bus_weight = 12650 # in kilograms, on Earth

print('On Earth, a double-decker bus weighs', bus_weight, 'kg')
print('The lightest a bus would be in the solar system is', bus_weight * min(gravity_on_planets), 'kg')
print('The heaviest a bus would be in the solar system is', bus_weight * max(gravity_on_planets), 'kg')

#Manipular datos de lista 
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planets_before_earth = planets[0:2] #slice
print(planets_before_earth)

planets_after_earth = planets[3:]
print(planets_after_earth)

#Unir listas (+)
amalthea_group = ['Metis', 'Adrastea', 'Amalthea', 'Thebe']
galilean_moons = ['Io', 'Europa', 'Ganymede', 'Callisto']

regular_satellite_moons = amalthea_group + galilean_moons
print('The regular satellite moons of Jupiter are', regular_satellite_moons)

#Ordenar listas sort()
regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

regular_satellite_moons.sort(reverse=True) #forma inversa
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

