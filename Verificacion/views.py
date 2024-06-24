#DJANGO MTV. Modelo ->Base de datos Template-> consultas que puede hacer el usuario View-> respuesta ante un link

from django.http import HttpResponse
import datetime
# ACA BAN LAS FUNCIONES VISTAS
# COMO ARGUMENTO TIENEN UNA REQUEST Y COMO RESPUESTA UN HTTP RESPONSE POR COMO TRABAJA DJANGO
#UNA URL VA A IR A ESTA VISTA QUE DEVUELVE UN TEXTO ->> IR A URLS.PY
def saludos (request):
    #pueden tener etiquetas html adentro
    return HttpResponse("Holaaaaa")



def fecha(request):
    fecha_actual = datetime.datetime.now()
    respuesta = f"Fecha actual: {fecha_actual.strftime('%Y-%m-%d %H:%M:%S')}"

    return HttpResponse(respuesta)

#VIEWS CON DOS PARAMETRS, el segundo lo voy a meter como el final de la url

def calculoedad(request,edad, agno):

    periodo = agno-2024
    edadFutura = edad+periodo
    documento = "<html><body><h2>En el año %s tendras %s años"%(agno, edadFutura)
    return HttpResponse(documento)