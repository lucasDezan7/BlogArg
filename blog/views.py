from django.shortcuts import render

def inicio(respuesta):
    return render(respuesta,'blog/inicio.html')
