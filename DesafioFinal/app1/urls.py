from django.urls import path
from .views import crear_celular, crear_notebook, crear_tele, buscar_tele, buscar_celular, buscar_notebook
from app1 import views 

urlpatterns = [
    #path('index/', home),
    path('', views.mostrar_index),
    path('crear_tele/', crear_tele, name = 'televisores_view'),
    path('crear_celular/', crear_celular, name = 'celulares_view'),
    path('crear_notebook/', crear_notebook, name = 'notebook_view'),
    path('buscar_tele/', buscar_tele, name = 'buscar_tele_view'),
    path('buscar_celular/', buscar_celular, name = 'buscar_celular_view'),
    path('buscar_notebook/', buscar_notebook, name = 'buscar_notebook_view'),
]


