from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
# Create your views here.

'''def egresos_totales (request):
    
    with connection.cursor() as cursor:
        
        cursor.execute('exec Indicadores.GastosTotales')
        
        resultado = cursor.fetchone()
        
        #solo devuelve un resultado
        
        response_data = {
            'egreso_totales': resultado[0]
        }
        
    return response_data

def ingresos_totales (request):
    
    with connection.cursor() as cursor:
        
        cursor.execute('exec Indicadores.ObtenerIngresosTotales')
        a
        resultado = cursor.fetchone()
        
        response_data = {
            
            'ingresos_totales' : resultado[0]
        }
    
    return response_data'''

def pedidos_totales(request):
    with connection.cursor() as cursor:
        
        cursor.execute('exec Indicadores.ObtenerPedidosTotales')

        resultado = cursor.fetchone()
        
        response_data = {
            'pedidos_totales': resultado[0]
        }
        
    return response_data

def ingresos_egresos_mensuales(request):
    # Mapeo de números a nombres de meses en español
    meses_espanol = {
        1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 
        5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto', 
        9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
    }
    
    with connection.cursor() as cursor:
        cursor.execute('exec Indicadores.IngresosVsEgresos')
        resultados = cursor.fetchall()
        
        data_requests = []
        for resultado in resultados:
            numero_mes = resultado[0]
            nombre_mes = meses_espanol.get(numero_mes, 'Mes desconocido')  # Obtenemos el nombre del mes

            data_requests.append({
                'mes': nombre_mes,  # Aquí usamos el nombre en español del mes
                'ingresos': resultado[2],
                'egresos': resultado[3],
            })

    return data_requests


def TasaCrecimiento(request):
    with connection.cursor() as cursor:
        cursor.execute('exec Indicadores.ObtenerTasasCrecimiento')
        
        resultado = cursor.fetchone()
        
        response_data = resultado[0]
    return response_data

def productos_mas_vendidos(request):
    with connection.cursor() as cursor:
        cursor.execute('exec Indicadores.ProductosMasVendidos')
        
        resultados = cursor.fetchall()
        response_data = []
        for resultado in resultados:
            response_data.append(
                {
                    'nombre' : resultado[0],
                    'cantidad' : resultado[1],
                }
            )
    return response_data

def obtener_indicadores_combinados(request):
    # Llamar a cada una de las funciones predefinidas y recoger sus datos
    
    pedidos_totales_data = pedidos_totales(request)
    ingresos_egresos_mensuales_data = ingresos_egresos_mensuales(request)
    tasa_crecimiento_data = TasaCrecimiento(request)
    productos_mas_vendidos_data = productos_mas_vendidos(request)

    # Crear el JSON de respuesta combinada
    response_data = {
        "ingresos_egresos_mensuales": ingresos_egresos_mensuales_data,
        "tasa_crecimiento": tasa_crecimiento_data,
        "pedidos_totales": pedidos_totales_data['pedidos_totales'],
        "productos_mas_vendidos": productos_mas_vendidos_data
    }

    # Devolver el JSON completo
    return JsonResponse(response_data, safe=False)