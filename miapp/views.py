from django.shortcuts import render

def saludo(request):
    return render(request, "turismo.html, contacto.html")