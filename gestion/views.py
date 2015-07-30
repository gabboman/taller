from django.shortcuts import render

# Create your views here.
from .models import Coches
from django.http import HttpResponse

def index(request):
    Ultimos5Coches = Coches.objects.order_by('-fecha_entrada')[:5]#Devuelve los coches ordenados por fecha de entrada, del mas nuevo al mas viejo (sin el - seria del mas viejo al mas nuevo)
    output = ', '.join([p.__str__() for p in Ultimos5Coches])#Los convierte a string
    return HttpResponse(output)#muestra el string en pantalla
#Con esto podemos realizar cálculos. Es necesario investigar acerca del html, ya que así enviamos solo texto sin html


def coche(request, coche_id):
    return HttpResponse("Estas mirando el coche %s." % coche_id)
