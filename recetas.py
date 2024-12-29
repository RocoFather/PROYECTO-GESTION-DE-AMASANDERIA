#recetas.py

#Contiene subprogramas para calcular la produccion diaria, 
#Mostrar la produccion diaria, Registro de ventas en la matriz,
#Mostrar las ventas realizas y Calculo de recetas

# Funciones para calcular produccon de cada tipo de pan
def repartir_recursos(recursos):
    recursos_repartidos = [
        recursos[0] / 8, recursos[1] / 8, recursos[2] / 8, 
        recursos[3] / 8, recursos[4] / 8, recursos[5] / 8
    ]
    return recursos_repartidos
#CALCULAR PRODUCCION DIARIA--------------------------------------
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
#MOSTRAR PRODUCCION DIARIA----------------------------------------------
def mostrar_produccion(produccion_diaria,pan_nombre):
    print("Produccion diaria:")
    for i in range(len(produccion_diaria)):
        print(f"{pan_nombre[i]}: {produccion_diaria[i]:.2f} kg")

#REGISTRAR VENTAS-------------------------------------------------------
def registrar_ventas(produccion_diaria,ventas_diarias,pan_nombre):
    print("Registro de ventas diarias:")
    for i in range(len(pan_nombre)):
        print(f"{i + 1}. {pan_nombre[i]}")
    tipo_pan = int(input("Seleccione el tipo de pan (1-8): ")) - 1
#valida que sea un valor correcto
    if tipo_pan < 0 or tipo_pan >= len(pan_nombre):
        print("Seleccione una opcion correcta porfavor. ")
        return
#elegir franja horaria
    print("1. Mañana    2. Tarde    3. Noche")
    horario = int(input("Seleccione la franja horaria (1-3): ")) - 1
#valida que sea un horario correcto
    if horario < 0 or horario >= 3:
        print("Franja horaria inválida.")
        return

    cantidad_vendida = float(input("Ingrese la cantidad vendida (kg): "))
#valida que una cantida correcta y no mayor a la produccion diaria
    if cantidad_vendida < 0 or cantidad_vendida > produccion_diaria[tipo_pan]:
        print("Cantidad inválida o excede la producción disponible.")
        return

    ventas_diarias[tipo_pan][horario] += cantidad_vendida
    produccion_diaria[tipo_pan] -= cantidad_vendida
    print("Venta registrada correctamente.")
    
#MOSTRAR VENTAS-----------------------------------------------------------
def mostrar_ventas(ventas_diarias,pan_nombre):
    horarios = ["Mañana","Tarde","Noche"]
    print("Ventas Diarias Realizadas: ")
    for i in range(len(ventas_diarias)):
        print(pan_nombre[i])
        for j in range(len(ventas_diarias[i])):
            print(f"  {horarios[j]}: {ventas_diarias[i][j]:.2f} kg")




#SUBPROGRAMAS DE RECETAS------------------------------------------------
#RECETAS MARRAQUETA
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
#RECETA HALLULLA
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
#RECETA DOBLADITAS
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
#RECETA DE CIABATTA
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
#RECETA PAN DE HOTDOG
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
#RECETA COLIZA
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
#RECETA PAN INTEGRAL
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
#RECETA HAMBURGUESA
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



