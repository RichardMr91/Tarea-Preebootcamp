#1.Multiplica por 2
def funcion1(a):
    lista=[]
    for i in range(0,a+1):
        x=i*2
        lista.append(x)
        continue
    return print(lista)

funcion1(8)

#2.Suma y resta: 

def funcion2(a):
    suma=a[0]+a[1]
    resta=a[0]-a[1]
    print(suma)
    return print(resta)

funcion2([5,4])

#3.Sumatoria menos longitud:


def sum_long(a):
    x=0
    for i in a:
        x=x+i
        continue
    resultado= x-len(a)
    return print(resultado)

sum_long([3])

#4. Valores multiplicados por el segundo
def mult_seg(a):
    lista3=[]
    x=0
    print(len(a))
    for i in a:
        if len(a)>1:
            x=i*a[1]
            lista3.append(x)
            continue
    return print(lista3)

mult_seg([32,3,4,5])


#.5 Valor multiplado y longitud


def mult_long(valor,log):
    lista4=[]
    x=0
    while len(lista4)<log:
        x=valor*log
        lista4.append(x)
        continue
    return print(lista4)

mult_long(7,5)







