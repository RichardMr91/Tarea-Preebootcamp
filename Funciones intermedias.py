
matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

ciudades = {
    "Mexico": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}

coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]
#1.actualizar valores en diccionarios

matriz[1]=[6,7,14]

print(matriz)

cantantes[0]={"nombre": "Enrique Martin Morales", "pais": "Puerto Rico"}

print (cantantes[0]["nombre"])

ciudades["Mexico"][2]="Monterrey"

print(ciudades)

coordenadas[0]["latitud"]=9.9355431

print (coordenadas[0]["latitud"])

#2. Iterar atraves de una lista de diccionarios

def iterardiccionario(a):
    for i in a:
        v=0
        while v<len(a):
            print(a[v])
            v+=1
        break

def iterardiccionario1(a):
    for i in a:
        v=0
        while v<len(i):
            print("nombre -",i["nombre"]+", pais -",i["pais"])
            v+=1
            break


iterardiccionario(cantantes)
iterardiccionario1(cantantes)
#3. Obtener valores de una lista de diccionarios
def iteraciondiccionario2(llave,lista):
    d=llave
    for i in lista:
        for x in i:
            print (i[d])
            break

iteraciondiccionario2("pais",cantantes)

#4. Iterar a traves de un diccionario con valores de lista
costa_rica1 = {
    "ciudades": ["San José", "Limón", "Cartago", "Puntarenas"],
    "comidas": ["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}

def imprimirinformacion(diccionario):
    for llaves in diccionario:
        c=0
        print(len(diccionario[llaves]), llaves)
        while c<len(diccionario[llaves]):
            print(diccionario[llaves][c])
            c+=1
        continue
imprimirinformacion(costa_rica1)