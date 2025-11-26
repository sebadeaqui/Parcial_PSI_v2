from django.urls import path
from . import views 
urlpatterns = [
    path("home/",views.saludo, name = "vistaPrincipal"),
    path("contacto/",views.contacto, name = "contacto")
]