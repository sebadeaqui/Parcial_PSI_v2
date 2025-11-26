from django.urls import path
from . import views 
urlpatterns = [
    path("home/",views.saludo, name = "vistaPrincipal"),
    path("contacto/",views.saludo, name = "contacto")
]