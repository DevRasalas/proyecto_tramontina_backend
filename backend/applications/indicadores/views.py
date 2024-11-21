from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
from .validador import *
from django.views.decorators.csrf import csrf_exempt
# Create your views here.



def pedidos_totales(request):
    with connection.cursor() as cursor:
        
        cursor.execute('exec RendimientoEmpresarial.[ObtenerPedidosTotales]')

        resultado = cursor.fetchone()
        
        response_data = {
            'pedidos_totales': int(resultado[0])
        }
        
    return response_data
def Obtener_Proveedores_Activos(request):
    with connection.cursor() as cursor:
        
        cursor.execute('exec [RendimientoEmpresarial].[ObtenerProveedoresActivos]')

        resultado = cursor.fetchone()
        
        if resultado is None or resultado[0] is None:
            response_data = int(0)
        else:
            response_data = int(resultado[0])
        
        
    return response_data

def ingresos_egresos_mensuales(request):
    # Mapeo de números a nombres de meses en español
    meses_espanol = {
        1: 'Enero', 2: 'Febrero', 3: 'Marzo', 4: 'Abril', 
        5: 'Mayo', 6: 'Junio', 7: 'Julio', 8: 'Agosto', 
        9: 'Septiembre', 10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
    }
    
    with connection.cursor() as cursor:
        cursor.execute('exec RendimientoEmpresarial.[IngresosVsEgresos]')
        resultados = cursor.fetchall()
        
        data_requests = []
        for resultado in resultados:
            
            numero_mes = resultado[0]
            nombre_mes = meses_espanol.get(numero_mes, 'Mes desconocido')  # Obtenemos el nombre del mes

            data_requests.append({
                'mes': nombre_mes,  # Aquí usamos el nombre en español del mes
                'ingresos': int(resultado[2]),
                'egresos': int(resultado[3]),
            })

    return data_requests


def Tasa_Crecimiento(request):
    with connection.cursor() as cursor:
        cursor.execute('exec RendimientoEmpresarial.[ObtenerTasasCrecimiento]')
        
        resultado = cursor.fetchone()

        if resultado is None or resultado[0] is None:
            response_data = 0.0
        else:
            response_data = float(resultado[0])
    return response_data

def productos_mas_vendidos(request):
    with connection.cursor() as cursor:
        cursor.execute('exec [RendimientoEmpresarial].[Top5ProductosMasVendidos]')
        
        resultados = cursor.fetchall()
        response_data = []
        for resultado in resultados:
            response_data.append(
                {
                    'nombre' : resultado[0],
                    'cantidad' : int(resultado[1]),
                }
            )
    return response_data

def Obtener_Stock_Total(request):
    with connection.cursor() as cursor:
        cursor.execute('exec RendimientoEmpresarial.ObtenerStockTotal')
        
        resultados = cursor.fetchone()
        if resultados is None or resultados[0] is None:
            response_data = 0.0
        else:
            response_data = float(resultados[0])
    return response_data

def Pagos_Pendientes_Por_Compra(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT [RendimientoEmpresarial].[ObtenerTotalPagosPendientes]();')
        
        resultados = cursor.fetchone()
        
        if resultados is None or resultados[0] is None:
            response_data = 0.0
        else:
            response_data = float(resultados[0])
    return response_data

def obtener_indicadores_combinados(request):
    # Llamar a cada una de las funciones predefinidas y recoger sus datos
    
    pedidos_totales_data = pedidos_totales(request)
    ingresos_egresos_mensuales_data = ingresos_egresos_mensuales(request)
    tasa_crecimiento_data = Tasa_Crecimiento(request)
    productos_mas_vendidos_data = productos_mas_vendidos(request)
    pagos_pendientes = Pagos_Pendientes_Por_Compra(request)
    proveedores_activos = Obtener_Proveedores_Activos(request)
    stock_productos = Obtener_Stock_Total(request)
    # Crear el JSON de respuesta combinada
    response_data = {
        "ingresos_egresos_mensuales": ingresos_egresos_mensuales_data,
        "tasa_crecimiento": tasa_crecimiento_data,
        "pedidos_totales": pedidos_totales_data['pedidos_totales'],
        "productos_mas_vendidos": productos_mas_vendidos_data,
        "pagos_pendientes": pagos_pendientes,
        "proveedores_activos": proveedores_activos,
        "stock_productos": stock_productos
    }

    # Devolver el JSON completo
    return JsonResponse(response_data, safe=False)

@csrf_exempt
def actualizar_tasacrecimiento(request):
    if request.method == 'POST':
        try:
            with connection.cursor() as cursor:
                cursor.execute("EXEC RendimientoEmpresarial.[ActualizarCrecimientoMensual]")
            return JsonResponse({'success': True, 'message': 'Proceso ejecutado correctamente.'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    else:
        return JsonResponse({'success': False, 'message': 'Método no permitido.'}, status=405)