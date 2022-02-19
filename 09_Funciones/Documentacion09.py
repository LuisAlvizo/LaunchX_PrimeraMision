#FUNCIONES

#Sin argumentos

#def para crear una funcion
# Defino mi función
from black import out


def rocket_parts():
    print('payload, propellant, structure')

# Llamo a mi función
rocket_parts()

output = rocket_parts()
print(output)

def rocket_parts2():
    return 'payload, propellant, structure'

output2= rocket_parts2()
print(output2)
 

#Argumentos
def distance_from_earth(destination):
    if destination == 'Moon':
        return '238,855'
    else:
        return 'Unable to compute to that destination'

print(distance_from_earth('Moon')) 
print(distance_from_earth('Saturn'))

#Varios Argumentos
def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

print(round(days_to_complete(238855, 75)))

#Argumentos de Palabra Clave
from datetime import timedelta, datetime

def arrival_time(hours=51):
    now = datetime.now() #datetime para definir la hor actual
    arrival = now + timedelta(hours=hours) #timedelta permite la operación de suma que da como resultado un objeto de hora nuevo
    return arrival.strftime('Arrival: %A %H:%M')

print(arrival_time())

print(arrival_time(hours=0))

#Combinación de Argumentos
from datetime import timedelta, datetime

def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f'{destination} Arrival: %A %H:%M')

print(arrival_time('Moon'))

print(arrival_time('Orbit', hours=0.13))

#Argumentos de Variable
def variable_length(*args):
    print(args)

print(variable_length())
print(variable_length('one', 'two'))
print(variable_length(None))


def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f'Total time to launch is {total_minutes} minutes'
    else:
        return f'Total time to launch is {total_minutes/60} hours'

print(sequence_time(4, 14, 18))
print(sequence_time(4, 14, 48))

#Argumentos de palabras clave variable
def variable_length(**kwargs):
    print(kwargs)
print(variable_length(tanks=1, day='Wednesday', pilots=3))

def crew_members(**kwargs):
    print(f'{len(kwargs)} astronauts assigned for this mission:')
    for title, name in kwargs.items():
        print(f'{title}: {name}')

print(crew_members(captain='Neil Armstrong', pilot='Buzz Aldrin', command_pilot='Michael Collins'))