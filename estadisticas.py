import matplotlib.pyplot as plt



def pan_mas_menos_vendido(ventas_diarias, pan_nombre):
  
    totales = [sum(ventas) for ventas in ventas_diarias]
    mas_vendido = max(totales)
    menos_vendido = min(totales)

    pan_mas_vendido = pan_nombre[totales.index(mas_vendido)]
    pan_menos_vendido = pan_nombre[totales.index(menos_vendido)]

    print(f"El pan más vendido fue: {pan_mas_vendido} con {mas_vendido:.2f} kg")
    print(f"El pan menos vendido fue : {pan_menos_vendido} con {menos_vendido:.2f} kg")
   


def franja_horaria_mas_y_menos_ventas():

def ganancia_e_inversion_total():

def ganancia_liquida_meta(): #?

def grafico_barras_ganancia():

def grafico_circular_ganancia_vs_costo():
    
#MENU D E ESTADISTICAS DONDE SE EJECUTARAN LAS ESTADISTICAS
def menu_estadisticas(produccion_diaria, ventas_diarias, meta_ganancia,precios_pan,precios_recursos,pan_nombre):
    while True:
        print("--------------Menu de Estadisticas--------------")
        print("1. Pan mas vendido y menos vendido")
        print("2. Franja horaria con mas ventas y Franja horaria con menos ventas")
        print("3. Ganancia total e inversion total")
        print("4. Ganancia liquida y meta")
        print("5. Grafico de barras de ganancias")
        print("6. Grafico circular de ganancia vs costo")
        print("7. Volver al menu principal")
        o = input("Seleccione una opcion: ")
        if o == "1":
            pan_mas_menos_vendido(ventas_diarias,pan_nombre)
        elif o == "2":
            franja_horaria_mas_y_menos_ventas(ventas_diarias)
        elif o == "3":
            ganancia_e_inversion_total()
        elif o == "4":
            ganancia_liquida_meta()
        elif o == "5":
            grafico_barras_ganancia
        elif o == "6":
            grafico_circular_ganancia_vs_costo()
        elif o == "7":
            break
        else:
            print("Ingrese una opcion valida porfavor")

#GENERADOR DE INFORME AL FINALIZAR
def finalizar_dia(ventas_diarias, produccion_diaria, meta_ganancia, contador_dia):
    informe = open(f"Informe dia {contador_dia}","w")
    informe.write()
    
        
        