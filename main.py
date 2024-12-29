#Programa principal
#Amasanderia importar recetas y estadisticas
import recetas
import estadisticas
import time as t
recursos_nombre: ["Harina","Agua","Levadura","Manteca","Azucar","Sal"]
recursos = [0,0,0,0,0,0]
recursos_repartidos = [0,0,0,0,0,0]
pan_nombre = ["Hallulla","Marraqueta","Dobladitas","Ciabatta"
              ,"Pan de completo","Coliza","Integral","Pan de hamburguesa"]
produccion_diaria = [0,0,0,0,0,0,0,0]
#matriz
ventas_diarias = [
  [0,0,0]
  [0,0,0]
  [0,0,0]
  [0,0,0]
  [0,0,0]
  [0,0,0]
  [0,0,0]
  [0,0,0]
]
meta_ganancia = 0
#funcion para registro diario
def inicio_registro():
  global recursos,produccion_diaria,meta_ganancia
  print("------Registro de recursos diarios------"")
  recursos[0] = float(input("Ingrese la cantidad de harina en kg: "))
  recursos[1] = float(input("Ingrese la cantidad de agua en kg: "))
  recursos[2] = float(input("Ingrese la cantidad de levadura en kg: "))
  recursos[3] = float(input("Ingrese la cantidad de manteca en kg: "))
  recursos[4] = float(input("Ingrese la cantidad de azucar en kg: "))
  recursos[5] = float(input("Ingrese la cantidad de sal en kg: "))
  meta_ganancia = float(input("Ingrese la meta de ganancia liquida: "))
  t.sleep(1)
  print("Calculando produccion_diaria")
  recursos_repartidos = recursos_repartidos(recursos)
  produccion_diaria = recetas.calcular_produccion_diaria(recursos_repartidos)
  t.sleep(1)
  print("Producción calculada con exito...")
  t.slepp(1)
  recetas.mostrar_produccion(produccion_diaria,pan_nombre)

  menu_dia()

#funcion menu control del dia
def menu_dia():
  while True:
    print("-------Menu del dia-------"")
    print("1. Registrar ventas"")
    print("2. Visualizar ventas registradas")
    print("3. Generar estadisticas")
    print("4. Finalizar dia y generar informe")
    print("5. Volver al menu principal"")
    o = input("Escoja una opcion (1-5):")
    if o == "1":
    
    elif o == "2":

    elif o == "3":

    elif o == "4":

    elif o == "5":
      break
    else:
      print("Opcion invalida, Intente de nuevo. ")

#Menu principal
while True:
  print("----------Sistema de Gestion de amasanderia----------"")
  print("1. Iniciar registro diario. ")
  print("2. Salir del sistema. ")
  o = input("Escoja una opcion (1/2): ")
  if o == "1":
    print("Iniciando registro diario. ")
    incio_registro()
  
  elif o == "2":
    print("Saliendo del sistema. ")
    break
  else:
    print("Porfavor Ingrese una opcion valida. ")
    