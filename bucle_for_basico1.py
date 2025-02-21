#1. Básico: imprime todos los números enteros del 0 al 100.
for i in range(0,101):
    print(i)

#2. Múltiples de 2: imprime todos los números múltiplos de 2 entre 2 y 500
for i in range(2,501,2):
    print(i)

"""3. Contando Vanilla Ice: imprime los números enteros del 1 al 100. 
Si es divisible por 5 imprime “ice ice” en vez del número. 
Si es divisible por 10, imprime “baby”"""

for i in range(1,101):
    if i%5==0 and i%10!=0:
        print('ice ice')
        continue
    if i%10==0:
        print('baby')
        continue
    print(i)

"""4. Wow. Número gigante a la vista: suma los números pares del 0 al 500,000 e imprime la suma total. 
(Sorpresa, será un número gigante). """

x=0

for i in range(0,500001,2):
        x=x+i
        continue
print (x)

#5. Regrésame al 3: imprime los números positivos comenzando desde 2024, en cuenta regresiva de 3 en 3.

x=2027
while x >=3:
    x=x-3
    print(x)

"""Contador dinámico: establece tres variables: numInicial, numFinal y multiplo. 
Comenzando en numInicial y pasando por numFinal, imprime los números enteros que sean múltiplos de multiplo. 
Por ejemplo: si numInicial = 3, numFinal = 10, y multiplo = 2, 
el bucle debería de imprimir 4, 6, 8, 10 (en líneas sucesivas)."""

numinicial= int(input("ingrese numero inicial: "))
numfinal= int(input("ingrese numero final: "))
multiplo= int(input("ingrese el multiplo: "))

for i in range(numinicial,numfinal+1):
    if i%multiplo==0:
        print(i)
        continue
    