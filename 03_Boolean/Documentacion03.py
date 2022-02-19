# Expresiones de prueba
a = 3
b = 10
# test expression / expresión de prueba
if a < b:
    # statement to be run / instrucción a ejecutar
    print(b)

#Declaraciones if
a = 93
b = 27
if a >= b:
    print(a)

a = 24
b = 44
if a <= 0:
    print(a)
print(b)

# else 
a = 93
b = 27
if a >= b:
    print(a)
else:
    print(b)

#elif (else if)
a = 93
b = 27
if a >= b:
    print("a es mayor o igual que b")
elif a == b:
    print("a es igual que b")

#Combinacion de declaraciones
a = 93
b = 27
if a > b:
    print("a es mayor que b")
elif a < b:
    print("a es menor que b")
else: 
    print ("a es igual que b")

#Lógica condicional anidada
a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print ("a es mayor que b y b es mayor que c")
    else: 
        print ("a es mayor que b y menor que c")
elif a == b:
    print ("a es igual que b")
else:
    print ("a es menor que b")

#Operador OR
a = 23
b = 34
if a == 34 or b == 34:
    print(a + b)

#Operador AND
a = 23
b = 34
if a == 34 and b == 34:
    print (a + b)