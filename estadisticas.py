import matplotlib.pyplot as plt


#PAN MAS VENDIDO Y MENOS VENDIDO
def pan_mas_menos_vendido(ventas_diarias, pan_nombre):
  
    totales = [sum(ventas) for ventas in ventas_diarias]
    mas_vendido = max(totales)
    menos_vendido = min(totales)

    pan_mas_vendido = pan_nombre[totales.index(mas_vendido)]
    pan_menos_vendido = pan_nombre[totales.index(menos_vendido)]

    print(f"El pan más vendido fue: {pan_mas_vendido} con {mas_vendido:.2f} kg")
    print(f"El pan menos vendido fue : {pan_menos_vendido} con {menos_vendido:.2f} kg")
#FRANJA HORARIA CON MAS Y MENOS VENTAS EN KG        
def franja_horaria_mas_menos_ventas(ventas_diarias):
 
    totales_por_franja = [sum(franja) for franja in zip(*ventas_diarias)]
    
    franja_mas_ventas = max(totales_por_franja)
    franja_menos_ventas = min(totales_por_franja)

    franjas = ["Mañana", "Tarde", "Noche"]
    
    print(f"Franja horaria con más ventas: {franjas[totales_por_franja.index(franja_mas_ventas)]} con {franja_mas_ventas:.2f} kg")
    print(f"Franja horaria con menos ventas: {franjas[totales_por_franja.index(franja_menos_ventas)]} con {franja_menos_ventas:.2f} kg")
#GANANCIA E INVERSION
def ganancia_e_inversion_total(ventas_diarias,recursos,precios_recursos,precios_pan):
    kilos_total = 0
    inversion_total = 0
    suma_cada_pan = []
    ganancia_cada_pan = []
    for fila in ventas_diarias:
        suma = 0
        for elemento in fila:
            suma += elemento
            kilos_total += elemento
            suma_cada_pan.append(suma)
    for i in recursos:
        inversion_total += recursos[i]*precios_recursos[i]
    for i in range(len(precios_pan)):
        ganancia = suma_cada_pan[i]*precios_pan[i]
        ganancia_cada_pan.append(ganancia)
    ganancia_total = sum(ganancia_cada_pan)
    print(f"LA GANANCIA TOTAL BRUTA ES {ganancia_total}$ ")
    print(f"LA INVERSION TOTAL FUE: {inversion_total}$ ")
#COMPARAACION CON META
def ganancia_liquida_meta(ventas_diarias,meta_ganancia,recursos,precios_recursos,precios_pan): 
    kilos_total = 0
    inversion_total = 0
    suma_cada_pan = []
    ganancia_cada_pan = []
    for fila in ventas_diarias:
        suma = 0
        for elemento in fila:
            suma += elemento
            kilos_total += elemento
            suma_cada_pan.append(suma)
    for i in recursos:
        inversion_total += recursos[i]*precios_recursos[i]
    for i in range(len(precios_pan)):
        ganancia = suma_cada_pan[i]*precios_pan[i]
        ganancia_cada_pan.append(ganancia)
    ganancia_total = sum(ganancia_cada_pan)
    ganancia_liquida = ganancia_total - inversion_total
    print(f"LA GANANCIA LIQUIDA ES {ganancia_liquida}$")
    if ganancia_liquida < meta_ganancia:
        print("LA META NO FUE SUPERADA:")
        print(f"{ganancia_liquida}/{meta_ganancia}")
    else:
        print("LA META FUE SUPERADA: ")
        print(f"{ganancia_liquida}/{meta_ganancia}")

#GRAFICO DE BARRAS
def grafico_barras_ganancia(ventas_diarias, precios_pan, pan_nombre): 
    ganancias = [] # Calcular las ganancias de cada tipo de pan 
    for i in range(len(ventas_diarias)): 
        total_ventas = sum(ventas_diarias[i]) 
        ganancia = total_ventas * precios_pan[i] 
        ganancias.append(ganancia) # Crear el grafico de barras 
    plt.bar(pan_nombre, ganancias, color='skyblue') 
    plt.xlabel("Tipo de Pan") 
    plt.ylabel("Ganancia ($)") 
    plt.title("Ganancias por Tipo de Pan") 
    plt.xticks(rotation=45) 
    plt.tight_layout() 
    plt.show()

#GRAFICO CIRCULAR
def grafico_circular_ganancia_vs_costo(ventas_diarias,recursos,precios_recursos,precios_pan):
    kilos_total = 0
    inversion_total = 0
    suma_cada_pan = []
    ganancia_cada_pan = []
    for fila in ventas_diarias:
        suma = 0
        for elemento in fila:
            suma += elemento
            kilos_total += elemento
            suma_cada_pan.append(suma)
    for i in recursos:
        inversion_total += recursos[i]*precios_recursos[i]
    for i in range(len(precios_pan)):
        ganancia = suma_cada_pan[i]*precios_pan[i]
        ganancia_cada_pan.append(ganancia)
    ganancia_total = sum(ganancia_cada_pan)
    etiquetas = ["Ganancia", "Inversión"]
    valores = [ganancia_total, inversion_total]

    plt.pie(valores, labels=etiquetas, autopct="%1.1f%%", startangle=90, colors=["green", "red"])
    plt.title("Distribución de Ganancia e Inversión")
    plt.axis("equal")
    plt.show()
    
#MENU D E ESTADISTICAS DONDE SE EJECUTARAN LAS ESTADISTICAS
def menu_estadisticas(recursos, ventas_diarias, meta_ganancia,precios_recursos,pan_nombre,precios_pan):
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
            franja_horaria_mas_menos_ventas(ventas_diarias)
        elif o == "3":
            ganancia_e_inversion_total(ventas_diarias,recursos,precios_recursos)
        elif o == "4":
            ganancia_liquida_meta(ventas_diarias,meta_ganancia,recursos,precios_recursos)
        elif o == "5":
            grafico_barras_ganancia(ventas_diarias,precios_pan, pan_nombre) 
        elif o == "6":
            grafico_circular_ganancia_vs_costo(ventas_diarias,recursos,precios_recursos,precios_pan)
        elif o == "7":
            break
        else:
            print("Ingrese una opcion valida porfavor")

#GENERADOR DE INFORME AL FINALIZAR
def finalizar_dia(ventas_diarias, meta_ganancia, contador_dia, precios_recursos, recursos,pan_nombre,precios_pan):
#calculos
    kilos_total = 0
    inversion_total = 0
    suma_cada_pan = []
    ganancia_cada_pan = []
    for fila in ventas_diarias:
        suma = 0
        for elemento in fila:
            suma += elemento
            kilos_total += elemento
            suma_cada_pan.append(suma)
    for i in recursos:
        inversion_total += recursos[i]*precios_recursos[i]
    for i in range(len(precios_pan)):
        ganancia = suma_cada_pan[i]*precios_pan[i]
        ganancia_cada_pan.append(ganancia)
    ganancia_total = sum(ganancia_cada_pan)
    ganancia_liquida = ganancia_total - inversion_total
    
    informe = open(f"Informe dia {contador_dia}","w")
    informe.write(f"-------INFORME DIA {contador_dia}-------\n")
    informe.write(f"GANANCIA BRUTA : {ganancia_total}$")
    informe.write(f"INVERSION DEL DIA : {inversion_total}$")
    informe.write(f"GANANCIA LIQUIDA : {ganancia_liquida}$")
    informe.write(f"GANANCIA Y META : {ganancia_liquida}/{meta_ganancia}")
    informe.write("---VENTA TOTAL DE CADA PAN---")
    for i in range(len(pan_nombre)):
        informe.write(f"{pan_nombre[i]} {suma_cada_pan[i]}$")
    print(f"Informe diario generado como (Informe dia {contador_dia}.txt) con exito. ")
    informe.close()
        
        