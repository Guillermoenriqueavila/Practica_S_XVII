from django.shortcuts import render
from .models import Cliente,Area,Empleado,Venta


#Creando la vista cliente
def Clientes(request):
 #obteniendo el dato cliente
    clientes=Cliente.objects.all()
    #obteniendo el dato area
    area=Area.objects.all()
    #obteniendo el dato empleado
    empleado=Empleado.objects.all()
    #obteniendo el dato venta
    venta=Venta.objects.all()

    return render(request, 'Clientes.html', {'clientes':clientes,'area':area,'empleado':empleado, 'venta':venta } )