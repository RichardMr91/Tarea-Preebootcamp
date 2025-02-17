numero1 = 70 #declaracion de variable
numero2 = 3.14 #declaracion de variable
booleano = False #revision de tipo 
cadena = 'Hola Mundo' #strings
ingredientes_pastel = ['Harina', 'Leche', 'Huevos', 'Vainilla', 'Chocolate'] #Lista inicializacion
persona = {'nombre': 'Patricio', 'pais': 'México', 'edad': 35, 'soltero': False} #diccionario inicializacion
frutas = ('guayaba', 'fresa', 'papaya') #tuplas inicializacion
print(type(frutas)) #revisión de tipo
print(ingredientes_pastel[2]) #lista accesar valor  
ingredientes_pastel.append('Mantequilla') #lista agregar valor
print(persona['nombre']) #diccionario accesar valor
persona['nombre'] = 'Kevin' #diccionario cambiar valor
persona['color_ojos'] = 'cafe' #diccionario agregar valor
print(frutas[2]) #tupla accesar valor 

if numero1 > 45: #condicional if
    print("Numero mayor")
else: #condicional else
    print("Numero menor")

if len(cadena) < 5: #condicional if, revision de tamaño
    print("Cadena corta")
elif len(cadena) > 15: #condicional else if, revision de tamaño
    print("Cadena larga")
else:
    print("Cadena perfecta")#condicional else

for x in range(8): #bucle for, incremento
    print(x)
for x in range(2,8): #bucle for, inicio, fin 
    print(x)
for x in range(2,8,2): #bucle for, inicio, fin
    print(x)
x = 0
while(x < 8): #bucle while, incremento
    print(x)
    x += 1

ingredientes_pastel.pop()  
ingredientes_pastel.pop(1) #eliminar leche de lista

print(persona)
persona.pop('color_ojos') #eliminar 'color_ojos' de diccionario
print(persona)

for ingrediente in ingredientes_pastel: #bucle for, inicio
    if ingrediente == 'Harina': #condicional if
        continue #bucle for, continue
    print('Después de la primera sentencia') 
    if ingrediente == 'Chocolate': #condicional if
        break #bucle for, break

def imprime_hola_10_veces():#definir funcion, argumento
    for numero in range(10): #parametro
        print('Hola1') 

imprime_hola_10_veces() #return

def imprime_hola_n_veces(n):#definir funcion, argumento
    for numero in range(n):#parametro
        print('Hola2')#funcion return

imprime_hola_n_veces(5)# return

def imprime_hola_n_o_diez_veces(n = 10):#definir funcion, argumento
    for numero in range(n): #parametro
        print('Hola3')

imprime_hola_n_o_diez_veces() #retur
imprime_hola_n_o_diez_veces(5)#return


"""
Sección BONUS
"""

# print(numero3)
# numero3 = 86
# frutas[0] = 'naranja'
# print(persona['hobbies'])
# print(ingredientes_pastel[11])
#   print(booleano)
# frutas.append('manzana')
# frutas.pop(1)