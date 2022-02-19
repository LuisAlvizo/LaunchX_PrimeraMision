#Inmutabilidad de las cadenas
from time import monotonic


fact = 'The Moon has no atmosphere.'
two_facts = fact + ' No sound can be heard on the Moon.'
print(two_facts)

#Uso de comillas
print('The "near side" is the part of the Moon that faces the Earth')
print("We only see about 60% of the Moon's surface")
print("""We only see about 60% of the Moon's surface, this is known as the "near side".""")

#Texto Multilinea (Salto de linea \n)
multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline) 

#Comillas triples
multiline = """Facts about the Moon:
...  There is no atmosphere.
...  There is no sound."""
print(multiline)

#Métodos string 
'temperatures and facts about the moon'.title()
heading = 'temperatures and facts about the moon'
heading.title()

#Dividir una cadena
temperatures = '''Daylight: 260 F
... Nighttime: -280 F'''
print(temperatures.split('\n'))

#Método .find() Buscar una cadena
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius,
... while Mars has -28 Celsius."""
print(temperatures.find('Moon'))
print(temperatures.find('Mars'))

#Minúsculas
print("The Moon And The Earth".lower())
#Mayúsculas
print('The Moon And The Earth'.upper())

#Extraer temperatura promedio
temperatures = 'Mars Average Temperature: -60 C'
parts = temperatures.split(':')
print(parts) #La cadena se divide en cuanto encuentra ':'
print(parts[-1]) #Devuelve el ultimo elemento

#Busca el valor numerico
mars_temperature = 'The highest temperature on Mars is about 30 C'
for item in mars_temperature.split():
    if item.isnumeric(): #.isdecimal()
        print(item)

'-60'.startswith('-') #Para valores negativos

#Verifica el ultimo caracter de una cadena
if "30 C".endswith("C"):
    print("This temperature is in Celsius")

#.replace() para buscar y reemplazar apariciones de un carácter o grupo de caracteres
print('Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius.'.replace('Celsius', 'C')) #Remplaza Celsius por una C

#Bucar una palabra
text = 'Temperatures on the Moon can vary wildly.'
'temperatures' in text
print('temperatures' in text.lower())

#método .join() puede volver a unir los caracteres.
moon_facts = ['The Moon is drifting away from the Earth.', 'On average, the Moon is moving about 4cm every year']
'\n'.join(moon_facts)

#Formato de cadenas
mass_percentage = '1/6'
print('On the Moon, you would weigh about %s of your weight on Earth' % mass_percentage)

print("""Both sides of the %s get the same amount of sunlight,
    but only one side is seen from %s because
    the %s rotates around its own axis when it orbits %s.""" % ('Moon', 'Earth', 'Moon', 'Earth'))

#Método Format
mass_percentage = '1/6'
print('On the Moon, you would weigh about {} of your weight on Earth'.format(mass_percentage))

print("""You are lighter on the {moon}, because on the {moon} 
... you would weigh about {mass} of your weight on Earth""".format(moon="Moon", mass=mass_percentage))

#Representar el valor 1/6 como un porcentaje con un decimal:
round(100/6, 1)

print(f'On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth')

subject = 'interesting facts about the moon'
print(f'{subject.title()}')