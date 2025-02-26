#1. Carga de Datos

ventas = [ 
    {"fecha": "2024-01-02","producto":"polera","cantidad": (2),"precio": (50.23)},
    {"fecha": "2024-03-23","producto":"pantalon","cantidad": (5),"precio": (60.13)},
    {"fecha": "2024-03-23","producto":"perfume","cantidad": (10),"precio": (80.45)},
    {"fecha": "2024-04-05","producto":"pantalon","cantidad": (6),"precio": (54)},
    {"fecha": "2024-04-05","producto":"zapatillas","cantidad": (1),"precio": (499.99)},
    {"fecha": "2024-06-18","producto":"polera","cantidad": (2),"precio": (23.99)},
    {"fecha": "2024-07-18","producto":"perfume","cantidad": (8),"precio": (23.99)}
    ]

#2.Cálculo de Ingresos Totales
def ingresostotales(a):
    monto=0
    for i in a:
        v=0
        montos=[]
        total=0
        while v<len(a):
            monto =a[v]["cantidad"]*a[v]["precio"]
            montos.append(monto)#se crea lista con los montos de todas las ventas realizadas
            v+=1
        break
    for i in montos:
        total=total+i#se suman los montos para conocer el total de las ventas realizadas
        continue
    
    print ("Ventas Totales:",round(total,2)) #se imprime el monto de ventas total

ingresostotales(ventas) 

#3.Análisis del Producto Más Vendido

def ventas_por_producto(a):
    ventas_por_producto_individual={}
    ventas_por_producto_lista=[]
    for i in a:
        v=0
        while v<len(a): #se crea lista de diccionarios con el nombre y la cantidad de cada venta
            nombre =i["producto"]
            cantidad=i["cantidad"]
            ventas_por_producto_individual={nombre:cantidad}
            ventas_por_producto_lista.append(ventas_por_producto_individual)
            v+=1
            break
    ventas_por_producto={}
    for d in ventas_por_producto_lista:#se suman la cantidad ventas de cada producto 
        for nombre, cantidad in d.items():
            if nombre in ventas_por_producto:
                ventas_por_producto[nombre] += cantidad
            else:
                ventas_por_producto[nombre] = cantidad
        
    #print(ventas_por_producto)

    res1 = max(ventas_por_producto, key=ventas_por_producto.get)#se recorre el diccionario para que retorne el producto con mas ventas
    return print ("El producto mas vendido:",res1,)

ventas_por_producto(ventas)


#4.Promedio de Precio por Producto

def precios_por_producto(c):
    precios_por_producto={}
    ventas_por_producto_lista=[]
    ventas_por_producto_individual=[]
    for i in c:
        v=0
        while v<len(c): #se crea lista de diccionarios {producto:(precio, cantidad de ventas)}
            nombre =i["producto"]
            tuplas=i["precio"]*i['cantidad'],i["cantidad"]
            ventas_por_producto_individual={nombre:tuplas}
            ventas_por_producto_lista.append(ventas_por_producto_individual)
            v+=1
            break
    #print (ventas_por_producto_lista)

    for diccionario in ventas_por_producto_lista:#se recorre lista y se suman los tuplas de cada venta de los productos (precio,cantidad)
        for nombre, tupla in diccionario.items():
            if nombre in precios_por_producto:
                precios_por_producto[nombre]= tuple(map(sum, zip(precios_por_producto[nombre], tupla)))
            else:
                precios_por_producto[nombre]= tupla
    #print(precios_por_producto)
    
    promedio_venta_individual={}
    promedio_venta=[]
    for nombre, tupla in precios_por_producto.items():
        promedio_venta_individual= {nombre:round(tupla[0]/tupla[1],2)}
        promedio_venta.append(promedio_venta_individual)
        
    print("precio promedio por producto:", promedio_venta)

precios_por_producto(ventas)

#5. Ventas por Día

def ingresos_por_dia(a):
    ingresos_por_dia_lista=[]
    ingresos_por_dia={}
    ventas1=[]
    for i in a:
        v=0
        while v<len(a):
            nombre =i["fecha"]
            cantidad=i["cantidad"]*i["precio"]
            ventas1={nombre:cantidad}
            ingresos_por_dia_lista.append(ventas1)
            v+=1
            break
    #print(ingresos_por_dia_lista)

    for d in ingresos_por_dia_lista:
        for nombre, cantidad in d.items():
            if nombre in ingresos_por_dia:
                ingresos_por_dia[nombre] += cantidad 
            else:
                ingresos_por_dia[nombre]= cantidad
            
    print("los Ingresos por dia fueron:",ingresos_por_dia)

ingresos_por_dia(ventas)

#6.Representación de Datos

def resumen_ventas(a):
    resumen_de_ventas1={}
    ventas_por_producto_lista=[]
    informacion={}
    resumen_ventas={}

    for i in a:
            nombre =i["producto"]
            informacion={"cantidad_vendida":i["cantidad"],
                        "ingresos totales":i["precio"]*i["cantidad"]
                        }
            ventas_por_producto_individual={nombre:informacion}
            ventas_por_producto_lista.append(ventas_por_producto_individual)
    #print(ventas_por_producto_lista)
    
    for d in ventas_por_producto_lista:
        for nombre, informacion in d.items():
            if nombre in resumen_de_ventas1:
                resumen_de_ventas1[nombre]['cantidad_vendida'] += informacion['cantidad_vendida']
                resumen_de_ventas1[nombre]['ingresos totales'] += informacion['ingresos totales']
            else:
                resumen_de_ventas1[nombre] = { 
                    'cantidad_vendida' : informacion['cantidad_vendida'],
                    'ingresos totales' : informacion['ingresos totales']
                    }
        #print(resumen_de_ventas1)

    for nombre, informacion in resumen_de_ventas1.items():
        cantidad_vendida = informacion['cantidad_vendida']
        ingresos_totales = informacion['ingresos totales']

        precio_promedio = ingresos_totales / cantidad_vendida

        detalle = {
        'cantidad vendida': cantidad_vendida,
        'ingresos totales': round(ingresos_totales,2),
        'Precio promedio': round(precio_promedio, 2)
        }

        resumen_ventas[nombre] = detalle
    
    print("El resumen de ventas:",resumen_ventas, "\n")
resumen_ventas(ventas)