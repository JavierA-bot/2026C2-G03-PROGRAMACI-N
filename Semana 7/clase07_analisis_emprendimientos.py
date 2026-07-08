"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""

from sedes import sedes

def calcular_total(lista_ventas):
    """Recibo una lista, la sumo y retorno el total."""
    return sum(lista_ventas)

def calcular_promedio(lista_ventas):
    """Retorno el promedio de ventas de la lista venta."""
    return sum(lista_ventas) / len(lista_ventas)

def calcular_porcentaje(total_ventas,meta): # total_ventas = total de ventas del emprendimiento
    """Calcula el procentaje de cumplimiento de la meta"""
    return total_ventas / meta * 100

def calular_clasificacion(porcentaje_logro):
    """Clasifica el emprendiemiento según porcentaje de cumplimiento de meta"""
    if porcentaje_logro >= 100:
        clasificacion_emprendimiento = "Meta alcanzada, emprendimiento rentable."
    elif porcentaje_logro >= 80:
        clasificacion_emprendimiento = "Observacion, no se logro la meta."
    else:
        clasificacion_emprendimiento = "Adventencia, problemas de rentabilidad. URGE ATENCIÓN."
    return clasificacion_emprendimiento

def imprimir_reporte(reporte):
    """Imprime el reporte final de ventas por sede"""
    print("\nREPORTE FINAL")
    print("-" * 60)
    for fila in reporte:
        print(f"Emprendimiento: {fila["nombre"]}".upper())
        print(f"Provincia: {fila["provincia"]}")
        print(f"Tipo: {fila["tipo"]}")
        print(f"Total semanal: ${fila["total"]:,.2f}")
        print(f"Promedio diario: ${fila["promedio"]:,.2f}")
        print(f"Pordentaje de Cumplimiento: {fila["porcentaje"]:,.0f}%")
        print(f"Clasificación: {fila["estado"]}")
        print("-" * 60)
    print(f"Cantidad de emprendimientos: {len(reporte)}")
    

#print("Cantidad de sedes", len(sedes))
#print(type(sedes), "vrs", type(sedes))
#print("Datos por sedes:", sedes[0].keys())

reporte = []
provincias = set()

for emprendimiento in sedes:
    #emprendimiento = sedes[0] #Extraigo primer emprendimiento de la lista
    ventas = emprendimiento["ventas"] #Extraigo las ventas del emprendimiento etiqueta
    meta = emprendimiento["meta"] #Extraigo la meta del emprendimiento

    total_emprendiento = calcular_total(ventas)
    promedio_emprendimiento = calcular_porcentaje(total_emprendiento,meta)
    promedio_diario = calcular_promedio(ventas)
    clasificacion = calular_clasificacion(promedio_emprendimiento)

    provincias.add(emprendimiento["provincia"]) #Crea la colección sin duplicar valores
    
    #print("\nEmprendimiento:", emprendimiento["nombre"])
    #print("Total de ventas:", total_emprendiento)
    #print("Porcentaje de ventas:", promedio_emprendimiento)
    #print("Promedio diario:", promedio_diario)
    #print("Análisis de emprendimiento:", clasificacion)
    reporte.append(
        {
            "nombre": emprendimiento["nombre"],
            "provincia": emprendimiento["provincia"],
            "tipo": emprendimiento["tipo"],   
            "total": total_emprendiento,
            "promedio": promedio_diario,
            "porcentaje": promedio_emprendimiento,
            "estado": clasificacion
            
        }
    )
#AL FINALIZAR FOR 
imprimir_reporte(reporte)

print(provincias)



