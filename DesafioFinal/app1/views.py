from django.shortcuts import render
from app1.form import *
from django.http import HttpResponse
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models.model import Televisores, Celulares, Notebooks
# Create your views here.

#def home(request):

#    return render(request, 'index.html')

def mostrar_index(request):

    return render(request, 'index.html')


def crear_tele(request):

    if request.method == 'POST':

        formulario = FormularioTele(request.POST)
        
        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data

            tele = Televisores(nombre=formulario_limpio['nombre'], precio=formulario_limpio['precio'])

            tele.save()

        return render(request, 'index.html')
        

    else:
        formulario = FormularioTele()

    return render(request, 'form.html', {'formulario' : formulario})

def crear_celular(request):
    if request.method == 'POST':

        formulario = FormularioCelular(request.POST)
        
        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data

            celular = Celulares(nombre=formulario_limpio['nombre'], precio=formulario_limpio['precio'])

            celular.save()

        return render(request, 'index.html')
        

    else:
        formulario = FormularioCelular()

    return render(request, 'form.html', {'formulario' : formulario})

def crear_notebook(request):
    if request.method == 'POST':

        formulario = FormularioNotebook(request.POST)
        
        if formulario.is_valid():
            formulario_limpio = formulario.cleaned_data

            notebooks = Notebooks(nombre=formulario_limpio['nombre'], precio=formulario_limpio['precio'])

            notebooks.save()

        return render(request, 'index.html')
        

    else:
        formulario = FormularioNotebook()

    return render(request, 'form.html', {'formulario' : formulario})




def buscar_tele(request):
    
    if request.GET.get('nombre', False):
        nombre = request.GET['nombre']
        
        televisor = Televisores.objects.filter(nombre__icontains=nombre)
        if not televisor:
            return render(request, 'view_data.html', {'respuesta': "No se encontraron datos"})
        return render(request, 'view_data.html', {'respuesta' : f"Se encontro el Producto: {televisor}"})

    else:
        respuesta = 'No hay datos'

    return render(request, 'view_data.html', {'respuesta': respuesta})


def buscar_celular(request):
    
    if request.GET.get('nombre', False):
        nombre = request.GET['nombre']
        
        celular = Celulares.objects.filter(nombre__icontains=nombre)
        if not celular:
            return render(request, 'view_data.html', {'respuesta': "No se encontraron datos"})
        return render(request, 'view_data.html', {'respuesta' : f"Se encontro el Producto: {celular}"})

    else:
        respuesta = 'No hay datos'

    return render(request, 'view_data.html', {'respuesta': respuesta})


def buscar_notebook(request):
    
    if request.GET.get('nombre', False):
        nombre = request.GET['nombre']
        
        notebook = Notebooks.objects.filter(nombre__icontains=nombre)
        if not notebook:
            return render(request, 'view_data.html', {'respuesta': "No se encontraron datos"})
        return render(request, 'view_data.html', {'respuesta' : f"Se encontro el Producto: {notebook}"})

    else:
        respuesta = 'No hay datos'

    return render(request, 'view_data.html', {'respuesta': respuesta})
