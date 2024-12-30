#Programa principal
#Amasanderia importar recetas y estadisticas
import recetas
import estadisticas
import time as t
#LISTAS CON NOMBRES
recursos_nombre: ["Harina","Agua","Levadura","Manteca","Azucar","Sal"] # type: ignore
pan_nombre = ["Hallulla","Marraqueta","Dobladitas","Ciabatta"
              ,"Pan de completo","Coliza","Integral","Pan de hamburguesa"]
#RECURSOS
recursos = [0,0,0,0,0,0]
recursos_repartidos = [0,0,0,0,0,0]
#PRODUCCION DIARIA
produccion_diaria = [0,0,0,0,0,0,0,0]
#MATRIZ DE VENTAS
# MATRIZ DE VENTAS
ventas_diarias = [
    [0.0, 0.0, 0.0],  # First row
    [0.0, 0.0, 0.0],  # Second row
    [0.0, 0.0, 0.0],  # Third row
    [0.0, 0.0, 0.0],  # Fourth row
    [0.0, 0.0, 0.0],  # Fifth row
    [0.0, 0.0, 0.0],  # Sixth row
    [0.0, 0.0, 0.0],  # Seventh row
    [0.0, 0.0, 0.0]   # Eighth row
]


#PRECIOS
precios_pan = [2190,2290,3190,3290,2990,3390,2850,2990]
precios_recursos = [50,1000,6000,2500,1500,400]
#META
meta_ganancia = 0
#Contador dias
contador_dia = 0

#funcion para registro diario
def inicio_registro():
    global recursos, produccion_diaria, meta_ganancia
    
    print("------Registro de recursos diarios------")
    
    for i, recurso in enumerate(["harina", "agua", "levadura", "manteca", "azúcar", "sal"]):
        while True:
            try:
                valor = float(input(f"Ingrese la cantidad de {recurso} en kg: "))
                if valor < 0:
                    print("Error: La cantidad no puede ser negativa. Intente de nuevo.")
                else:
                    recursos[i] = valor
                    break
            except ValueError:
                print("Error: Por favor ingrese un número válido. Intente de nuevo.")

    while True:
        try:
            meta_ganancia = float(input("Ingrese la meta de ganancia líquida: "))
            if meta_ganancia < 0:
                print("Error: La meta de ganancia no puede ser negativa. Intente de nuevo.")
            else:
                break
        except ValueError:
            print("Error: Por favor ingrese un número válido. Intente de nuevo.")

    
    t.sleep(1)
    print("Calculando producción diaria...")
    
    recursos_repartidos = recetas.repartir_recursos(recursos)
    produccion_diaria = recetas.calcular_produccion_diaria(recursos_repartidos)
    
    t.sleep(1)
    print("Producción calculada con éxito...")
    
    t.sleep(1)
    recetas.mostrar_produccion(produccion_diaria, pan_nombre)
  
    menu_dia()


#funcion menu control del dia
def menu_dia():
    global contador_dia
    while True:
        print("-------Menu del dia-------")
        print("1. Registrar ventas")
        print("2. Visualizar ventas registradas")
        print("3. Generar estadisticas")
        print("4. Finalizar dia y generar informe")
        print("5. Volver al menu principal")
        o = input("Escoja una opcion (1-5):")
        if o == "1":
            try:
                recetas.registrar_ventas(produccion_diaria,ventas_diarias,pan_nombre)
            except ValueError:
                print("Error: porfavor ingrese un valor valido.")
        
        elif o == "2":
            try:
                 recetas.mostrar_ventas(ventas_diarias,pan_nombre)
            except Exception as e:
                print(f"Error al mostrar las ventas: {e}")
        elif o == "3":
             try:
                 estadisticas.menu_estadisticas(recursos, ventas_diarias, meta_ganancia,precios_recursos,pan_nombre,precios_pan)
             except Exception as e:
                print(f"Error al generar estadisticas: {e}")
        elif o == "4":
            o2 = input("Esta seguro de terminar el dia y generar el informe? (si/no): ")
            if o2.lower() == "si":
                contador_dia += 1
                try:
                  estadisticas.finalizar_dia(ventas_diarias, produccion_diaria, meta_ganancia, contador_dia, precios_recursos, recursos,pan_nombre)
                except Exception as e:
                    print(f"Error al finalizar el dia: {e}")
                break
            elif o2.lower() == "no":
                pass
            else:
                print("Opcion no valida.")
                pass

        elif o == "5":
            break
        else:
            print("Opcion invalida, Intente de nuevo. ")

#Menu principal
while True:
    print("----------Sistema de Gestion de amasanderia----------")
    print("1. Iniciar registro diario. ")
    print("2. Salir del sistema. ")
    o = input("Escoja una opcion (1/2): ")
    if o == "1":
        print("Iniciando registro diario. ")
        inicio_registro()
    
    elif o == "2":
        print("Saliendo del sistema. ")
        break
    else:
        print("Porfavor Ingrese una opcion valida. ")
    
