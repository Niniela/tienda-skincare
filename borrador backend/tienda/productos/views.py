from django.shortcuts import render
from .models import Producto

# Create your views here.

def listar (request):
    print("Hola estoy en listar")
    alumnos=Producto.objects.all()
    context={'productos':producto}
    return render(request,'producto/listar.html',context)


