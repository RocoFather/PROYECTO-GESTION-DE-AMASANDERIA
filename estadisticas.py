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
