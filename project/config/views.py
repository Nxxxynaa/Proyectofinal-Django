from django.http import HttpResponse


def saludo(request):
    return HttpResponse("Holaa")


def saludo2(request):

    nombre = input("*** Ingresa tu nombre: ")

    return HttpResponse(f"Hola <h1> {nombre} </h1>")


def nombre(request, nombre: str, apellido: str):

    return HttpResponse(f"{apellido.upper()}, {nombre}")    
