#recetas.py
# Funciones para calcular produccon de cada tipo de pan
def repartir_recursos(recursos):
    recursos_repartidos = [
        recursos[0] / 8, recursos[1] / 8, recursos[2] / 8, 
        recursos[3] / 8, recursos[4] / 8, recursos[5] / 8
    ]
    return recursos_repartidos
#CALCULAR PRODUCCION DIARIA
def calcular_produccion_diaria(recursos_repartidos):

    hallulla = calcular_hallulla(recursos_repartidos)
    marraqueta = calcular_marraqueta(recursos_repartidos)
    dobladitas = calcular_dobladitas(recursos_repartidos)
    ciabatta = calcular_ciabatta(recursos_repartidos)
    hot_dog = calcular_hotdog(recursos_repartidos)
    coliza = calcular_coliza(recursos_repartidos)
    integral = calcular_integral(recursos_repartidos)
    hamburguesa = calcular_hamburguesa(recursos_repartidos)

    produccion_diaria = [
        hallulla, marraqueta, dobladitas, ciabatta,
        hot_dog, coliza, integral, hamburguesa
    ]

    return produccion_diaria
#MOSTRAR PRODUCCION DIARIA
def mostrar_produccion(produccion_diaria,pan_nombre):
    print("Produccion diaria:")
    for i in range(len(produccion_diaria)):
        print(f"{pan_nombre[i]}: {produccion_diaria[i]:.2f} kg")

#REGISTRAR VENTAS
def registrar_ventas(produccion_diaria,ventas_diarias,pan_nombre):
    print("Registro de ventas diarias:")
    for i in range(len(produccion_diaria)):
        venta = ventas_diarias[i]
        if venta > produccion_diaria[i]:
            print(f" No hay suficiente {pan_nombre[i]} disponible. Venta ajustada a {produccion_diaria[i]:.2f} kg.")
            ventas_diarias[i] = produccion_diaria[i]
        else:
            print(f"{pan_nombre[i]}: Venta registrada de {venta:.2f} kg.")
        produccion_diaria[i] -= ventas_diarias[i]
    return produccion_diaria
    
    





#RECETAS DE PAN
def calcular_marraqueta(recursos_repartidos):
    agua, harina, levadura, manteca, azucar, sal = recursos_repartidos

    agua = agua / 0.4
    harina = harina / 0.65
    levadura = levadura / 0.03
    manteca = manteca / 0.02
    azucar = azucar / 0.02
    sal = sal / 0.01

    cantidad_marraquetas = min(agua,harina,levadura,manteca,azucar,sal)

    return cantidad_marraquetas

def calcular_hallulla(recursos_repartidos):
    agua, harina, levadura, manteca, azucar, sal = recursos_repartidos

    agua = agua / 0.35
    harina = harina / 0.6
    levadura = levadura / 0.02
    manteca = manteca / 0.05
    azucar = azucar / 0.03
    sal = sal / 0.01

    cantidad_hallulas = min(agua, harina, levadura, manteca, azucar, sal)

    return cantidad_hallulas

def calcular_dobladitas(recursos_repartidos):
    agua, harina, levadura, manteca, azucar, sal = recursos_repartidos

    agua = agua / 0.3
    harina = harina / 0.55
    levadura = levadura / 0.015
    manteca = manteca / 0.08
    azucar = azucar / 0.05
    sal = sal / 0.01

    cantidad_dobladitas = min(agua, harina, levadura, manteca, azucar, sal)

    return cantidad_dobladitas

def calcular_ciabatta(recursos_repartidos):
    agua, harina, levadura, manteca, azucar, sal = recursos_repartidos

    agua = agua / 0.5
    harina = harina / 0.75
    levadura = levadura / 0.02
    manteca = manteca / 0.01
    azucar = azucar / 0.01
    sal = sal / 0.015

    cantidad_ciabatta = min(agua, harina, levadura, manteca, azucar, sal)

    return cantidad_ciabatta

def calcular_hotdog(recursos_repartidos):
    agua, harina, levadura, manteca, azucar, sal = recursos_repartidos

    agua = agua / 0.4
    harina = harina / 0.7
    levadura = levadura / 0.025
    manteca = manteca / 0.03
    azucar = azucar / 0.04
    sal = sal / 0.01

    cantidad_hotdog = min(agua, harina, levadura, manteca, azucar, sal)

    return cantidad_hotdog

def calcular_coliza(recursos_repartidos):
    agua, harina, levadura, manteca, azucar, sal = recursos_repartidos

    agua = agua / 0.35
    harina = harina / 0.6
    levadura = levadura / 0.02
    manteca = manteca / 0.05
    azucar = azucar / 0.03
    sal = sal / 0.01

    cantidad_coliza = min(agua, harina, levadura, manteca, azucar, sal)

    return cantidad_coliza

def calcular_integral(recursos_repartidos):
    agua, harina, levadura, manteca, azucar, sal = recursos_repartidos

    agua = agua / 0.4
    harina = harina / 0.7
    levadura = levadura / 0.02
    manteca = manteca / 0.03
    azucar = azucar / 0.02
    sal = sal / 0.02

    cantidad_integral = min(agua, harina, levadura, manteca, azucar, sal)

    return cantidad_integral

def calcular_hamburguesa(recursos_repartidos):
    agua, harina, levadura, manteca, azucar, sal = recursos_repartidos

    agua = agua / 0.35
    harina = harina / 0.65
    levadura = levadura / 0.025
    manteca = manteca / 0.04
    azucar = azucar / 0.05
    sal = sal / 0.01

    cantidad_hamburguesa = min(agua, harina, levadura, manteca, azucar, sal)

    return cantidad_hamburguesa




