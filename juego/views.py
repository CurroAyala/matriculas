from django.shortcuts import render


def inicio(request):
    """
    Esta vista se encarga de renderizar la página de inicio.
    """
    return render(request, 'juego/inicio.html')