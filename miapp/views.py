from django.shortcuts import render

def saludo(request):
    return render(request, "turismo.html")

def contacto(request):
    return render(request, "contacto.html")


