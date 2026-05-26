# Trabajo Codigo Fase 5
# Autor: Andres Tellez 
# Fecha: 23/05/2026
# Problema: 3
# Descripcion: Analizar inventario y determinar que articulos necesitan ser reabastecidos.

inventario = [
    {"codigo": "A1", "nombre": "Mouse", "cantidad": 3, "minimo": 10},
    {"codigo": "A2", "nombre": "Teclado", "cantidad": 3, "minimo": 10},
    {"codigo": "A3", "nombre": "Monitor", "cantidad": 8, "minimo": 10},
    {"codigo": "A4", "nombre": "Impresora", "cantidad": 2, "minimo": 10},
    {"codigo": "A5", "nombre": "Laptop", "cantidad": 3, "minimo": 10}
]

def calcular_pedido(stock_actual, stock_minimo):
    if stock_actual < stock_minimo:
        cantidad = stock_minimo - stock_actual
    else:
        cantidad = 0
    return cantidad 

print("REPORTE DE REABASTECIMIENTO DE INVENTARIO")
print("-----------------------------------------")

for articulo in inventario:
    
    codigo = articulo["codigo"]
    nombre = articulo["nombre"]
    stock_actual = articulo["cantidad"]
    stock_minimo = articulo["minimo"]
    
    pedido = calcular_pedido(stock_actual, stock_minimo)
    
    print("Ariculo:", nombre)
    print("Cantidad a pedir:", pedido)
    print("-----------------------------------------")